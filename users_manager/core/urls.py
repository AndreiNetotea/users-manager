from django.urls import path
from users_manager.core import views

urlpatterns = [
    path('', views.index, name='users'),
    path('upload/', views.upload_cv, name='add_user'),
    path('users/', views.users_list, name='users_list'),
    path('users/upload/', views.upload_cv, name='upload_cv'),
    path('users/<int:pk>/', views.delete_user, name='delete_user'),
    path('class/users/', views.UserListView.as_view(), name='class_users_list'),
    path('class/users/upload/', views.UploadCvView.as_view(), name='ad_cv'),
    path('user-details/<int:id>', views.user_details, name='user_details'),
    path('profile-page', views.profile_page, name='profile-page'),
    path('jobs', views.jobs, name='jobs'),
    path('add-job', views.add_job, name='add-job'),
    path('appointments', views.appointments, name='appointments'),
    path('add-appointment', views.add_appointment, name='add-appointment'),
]