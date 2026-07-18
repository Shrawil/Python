from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_view, name='department_view'),
    path('add/', views.add_dep, name='add_dep'),
]