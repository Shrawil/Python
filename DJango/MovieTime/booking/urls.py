from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="booking"),
    path("book/<int:movie_id>/", views.book_movie, name="book_movie"),
]