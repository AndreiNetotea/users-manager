from django.urls import path
from users_manager.authentication import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('register', views.register_view, name='register')
]