from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('me/', views.profile_view, name='me'),
    path("search/", views.search_view, name='search'),
    path("delete-post/<int:post_id>/", views.delete_post, name="delete_post"),
    path("user/<str:username>/", views.user_profile, name='user_profile'),
    path(
        "follow/<str:username>/",
        views.follow_user,
        name="follow"
    ),

    path(
        "unfollow/<str:username>/",
        views.unfollow_user,
        name="unfollow"
    ),
    path('edit/', views.edit_view, name='edit'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)