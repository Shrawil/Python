from django.urls import path
from . import views

urlpatterns = [
    path("chat/", views.chat_list, name="chat_list"),
    path("chat/<str:username>/", views.chat, name="chat"),
    path('chat/<str:username>/poll/', views.poll_messages, name='poll_messages'),
]