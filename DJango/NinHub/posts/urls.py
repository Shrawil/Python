from django.urls import path
from . import views

urlpatterns = [
    path("create-post/", 
        views.create_post, 
        name="create-post"
    ),
    path("like-post/<int:post_id>/",
        views.like_post, 
        name="like_post"
    ),
    path(
        "comment/<int:post_id>/",
        views.add_comment,
        name="add_comment"
    ),
]