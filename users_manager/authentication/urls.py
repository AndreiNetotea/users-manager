from django.urls import path
from users_manager.authentication import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('accounts/login', views.login_view, name='login'),
    path('logout', views.logout_view, {'next': ''}, name='logout'),
    path('accounts/logout', views.logout_view, {'next': ''}, name='logout'),
    path('register', views.register_view, name='register')
]