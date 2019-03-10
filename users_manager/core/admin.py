from django.contrib import admin
from .models import UserProfile

# Register your models here.

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'updated_at', 'cv', 'image')
    search_fields = ('id', 'name')



admin.site.register(UserProfile, UserProfileAdmin)