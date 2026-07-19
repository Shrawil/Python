from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_view, name='show_dep'),
    path('add/', views.add_dep, name='add_dep'),
]