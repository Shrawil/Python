from social.models import Follow
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import ProfileForm
from user.models import Profile
from posts.models import Post, Like
from posts.forms import CommentForm
from django.db.models import Count

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else: 
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form':form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'Invalid Credentials!'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home_view(request):
    profile = Profile.objects.get(user=request.user)
    posts = Post.objects.all().order_by("-created_at")  
    liked_posts = set(
        Like.objects.filter(user=request.user)
        .values_list("post_id", flat=True)
    )

    already_following_ids = Follow.objects.filter(
        follower=request.user
    ).values_list("following_id", flat=True)

    suggested_users = (
        User.objects.exclude(id=request.user.id)
        .exclude(id__in=already_following_ids)
        .annotate(follower_count=Count("follower"))
        .order_by("-follower_count")[:5]
    )
    
    return render(request, "user/home.html", {
        "posts": posts,
        "liked_posts": liked_posts,
        "profile": profile,
        "comment_form": CommentForm(),
        "suggested_users":suggested_users,
    })

@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'user/profile.html', {'profile':profile, 'is_me':True})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.user != request.user:
        return redirect("me")

    if request.method == "POST":
        post.delete()

    return redirect("me")

@login_required
def edit_view(request):

    profile = request.user.profile

    if request.method == "POST":

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect("me")

    else:
        form = ProfileForm(instance=profile)

    return render(request, "user/edit.html", {
        "form": form
    })

@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    is_me = (request.user == user)

    is_following = Follow.objects.filter(
        follower=request.user,
        following=user
    ).exists()

    return render(request, "user/profile.html", {'profile': user.profile, 'is_me':is_me, 'is_following':is_following})

@login_required
def follow_user(request, username):
    if request.method != "POST":
        return redirect("user_profile", username=username)

    user = get_object_or_404(User, username=username)

    if request.user != user:
        Follow.objects.get_or_create(
            follower=request.user,
            following=user,
        )

    next_page = request.GET.get("next")

    if next_page == "home":
        return redirect("home")

    return redirect("user_profile", username=username)

@login_required
def unfollow_user(request, username):
    if request.method != "POST":
        return redirect("user_profile", username=username)
    
    user = get_object_or_404(User, username=username)

    Follow.objects.filter(
        follower=request.user,
        following=user
    ).delete()

    return redirect("user_profile", username=username)


@login_required
def search_view(request):
    query = request.GET.get("q", "")
    users = User.objects.none()
    if query:
        users = User.objects.filter(
            username__icontains=query
        )
    return render(request, "user/search.html", {
        "query": query,
        "users": users,
    })