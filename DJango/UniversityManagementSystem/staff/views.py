from django.shortcuts import render, redirect
from .models import Staff
from .forms import StaffForm

def add_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_staff')
    else:
        form = StaffForm()
    context = {'form':form}
    return render(request, 'staff/add_staff.html', context)

def staff_views(request):
    staff = Staff.objects.all()
    context = {'staff':staff}
    return render(request, 'staff/show_staff.html', context)