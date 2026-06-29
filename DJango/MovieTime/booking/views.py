from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from catalog.models import Movies
from .models import Booking, Show
from django.contrib import messages

@login_required
def index(request):
    return render(request, "booking/index.html")

@login_required
def book_movie(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    shows = Show.objects.filter(movie=movie)

    if request.method == "POST":
        show_id = request.POST.get("show")
        seats = request.POST.get("seats")

        selected_show = get_object_or_404(Show, id=show_id)

        Booking.objects.create(
            user=request.user,
            show=selected_show,
            seats=seats
        )

        messages.success(
            request,
            f"Booked {seats} seat(s) for {selected_show.movie.name} successfully!"
        )

        return redirect("index")
    if not shows.exists():
        return render(request, "booking/book.html", {
            "movie": movie,
            "shows": [],
            "error": "No shows available for this movie."
        })
    return render(request, "booking/book.html", {
        "movie": movie,
        "shows": shows,
    })