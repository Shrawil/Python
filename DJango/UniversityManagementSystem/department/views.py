from django.shortcuts import render, redirect
# Will need this later
from django.contrib.auth.decorators import login_required
from .models import Department
from .forms import DepartmentForm
# Create your views here.

def add_dep(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('show_dep')
    else: 
        form = DepartmentForm()
    
    context = {'form': form}
    return render(request, 'department/add_dep.html', context)

def department_view(request):
    # Get all objects stored inside Department model.
    departments = Department.objects.all()
    context = {'departments':departments}
    return render(request, 'department/show_dep.html', context)