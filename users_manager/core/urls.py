from django.urls import path
from users_manager.core import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-user/', views.add_user, name='upload_cv'),
    path('users/', views.users_list, name='users_list'),
    path('users/upload/', views.upload_cv, name='add_user'),
    path('users/<int:pk>/', views.delete_user, name='delete_user'),
    path('class/users/', views.UserListView.as_view(), name='class_users_list'),
    path('class/users/upload/', views.UploadCvView.as_view(), name='ad_cv'),
    path('user-details/<int:id>', views.user_details, name='user_details')
]