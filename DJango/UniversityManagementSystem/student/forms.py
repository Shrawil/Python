from django import forms 
from .models import Students

class StudentForms(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['student_name', 'student_age', 'student_email', 'student_year', 'department']