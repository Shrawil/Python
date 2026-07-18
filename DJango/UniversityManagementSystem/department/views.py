from django.shortcuts import render
# Will need this later
from django.contrib.auth.decorators import login_required
from .models import Department
# Create your views here.

def add_dep(request):
    return render(request, 'department/add_dep.html')

def department_view(request):
    # Get all objects stored inside Department model.
    departments = Department.objects.all()
    context = {'departments':departments}
    return render(request, 'department/show_dep.html', context)