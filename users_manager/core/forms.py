from django import forms

from .models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'email', 'description', 'cv', 'image')
