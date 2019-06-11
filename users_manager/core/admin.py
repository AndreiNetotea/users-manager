from django.contrib import admin
from .models import UserProfile, Job, Appointment

# Register your models here.

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'job', 'country', 'city', 'phone_number', 'description', 'cv', 'image')
    search_fields = ('id', 'name')

class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'salary')
    search_fields = ('id', 'name')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date')
    search_fields = ('id', 'date')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Appointment, AppointmentAdmin)