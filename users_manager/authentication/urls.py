from django.urls import path
from users_manager.core import views

urlpatterns = [
    path('login', views.users_list, name='users_list'),

]