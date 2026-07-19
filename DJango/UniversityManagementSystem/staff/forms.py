from django import forms
from .models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff 
        fields = ['staff_name' ,'staff_role', 'department']