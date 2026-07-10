from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils.dateparse import parse_datetime
from .models import Message, Notification

@login_required
def chat(request, username):
    other_user = get_object_or_404(User, username=username)

    if request.method == "POST":
        text = request.POST.get("message", "").strip()
        if text:
            Message.objects.create(sender=request.user, receiver=other_user, text=text)

            # one open notification per sender, refreshed rather than duplicated
            Notification.objects.update_or_create(
                user=other_user,
                sender=request.user,
                notif_type="message",
                is_read=False,
                defaults={"text": f"New message from {request.user.username}"},
            )
        if request.headers.get("X-Requested-With") != "XMLHttpRequest":
            return redirect("chat", username=username)
        return JsonResponse({"status": "ok"})

    # opening the thread marks their messages + notification as read
    Message.objects.filter(sender=other_user, receiver=request.user, is_read=False).update(is_read=True)
    Notification.objects.filter(user=request.user, sender=other_user, is_read=False).update(is_read=True)

    messages = Message.objects.filter(
        Q(sender=request.user, receiver=other_user) | Q(sender=other_user, receiver=request.user)
    )
    return render(request, "social/chat.html", {"other_user": other_user, "messages": messages})

@login_required
def chat_list(request):
    messages = Message.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user)
    ).select_related("sender", "receiver").order_by("-created_at")  # newest first

    chat_data = []
    seen = {}

    for message in messages:
        other_user = (
            message.receiver if message.sender == request.user else message.sender
        )

        if other_user.id not in seen:
            unread_count = Message.objects.filter(
                sender=other_user, receiver=request.user, is_read=False
            ).count()

            entry = {
                "user": other_user,
                "last_message": message.text,
                "last_time": message.created_at,
                "unread_count": unread_count,
            }
            seen[other_user.id] = entry
            chat_data.append(entry)

    context = {
        "chat_data": chat_data
    }
    return render(request, "social/chat_list.html", context)

def poll_messages(request, username):
    other_user = User.objects.get(username=username)
    after_id = request.GET.get('after_id', 0)

    msgs = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user],
        id__gt=after_id,
    ).order_by('id')

    data = [
        {
            'id': m.id,
            'sender': m.sender.username,
            'text': m.text,
            'is_me': m.sender_id == request.user.id,
        }
        for m in msgs
    ]
    return JsonResponse({'messages': data})