from django import forms
from .models import Post
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["image", "caption"]
        widgets = {
            "image": forms.ClearableFileInput(attrs={"id": "id_image", "accept": "image/*"}),
            "caption": forms.Textarea(attrs={"placeholder": "Write a caption..."}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": forms.TextInput(attrs={
                "placeholder": "Add a comment...",
                "autocomplete":"off",
            })
        }