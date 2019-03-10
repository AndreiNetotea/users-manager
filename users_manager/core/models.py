from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    cv = models.FileField(upload_to='users/cvs/', blank=True)
    image = models.ImageField(upload_to='users/photos/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name