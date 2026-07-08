from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["pfp", "bio", "website", "location"]

        widgets = {
            "pfp": forms.FileInput(attrs={
                "id": "id_pfp",
                "hidden": True,
                "accept": "image/*",
            }),
            "bio": forms.Textarea(attrs={
                "rows": 4,
                "class": "form-input"
            }),
            "website": forms.URLInput(attrs={
                "class": "form-input",
                "placeholder": "https://example.com"
            }),
            "location": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Your location"
            }),
        }

class RegisterForm(UserCreationForm):
    pass