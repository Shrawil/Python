from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_students, name='show_students'),
    path('add_students/', views.add_students, name='add_students'),
]
