from django.contrib import admin
from .models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'phone_number', 'address',
                    'created_at', 'updated_at')
    search_fields = ('id', 'user', 'phone_number')