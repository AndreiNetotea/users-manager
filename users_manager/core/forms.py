from django import forms

from .models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'email', 'job', 'country', 'city', 'phone_number', 'description', 'cv', 'image')
