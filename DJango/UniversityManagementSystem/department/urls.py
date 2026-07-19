from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_view, name='show_dep'),
    path('add_department/', views.add_dep, name='add_dep'),
]