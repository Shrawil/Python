from django.shortcuts import render, redirect 
from .models import Students
from .forms import StudentForms

def show_students(request):
    students = Students.objects.all()
    return render(request, 'student/show_students.html', {'students':students})

def add_students(request):
    if request.method == 'POST':
        form = StudentForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_students')
    else:
        form = StudentForms()
    return render(request, 'students/add_students.html', {'forms':form})