from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from users_manager.core import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('add-user/', views.add_user, name='upload_cv'),
    path('users/', views.users_list, name='users_list'),
    path('users/upload/', views.upload_cv, name='add_user'),
    path('users/<int:pk>/', views.delete_user, name='delete_user'),

    path('class/users/', views.UserListView.as_view(), name='class_users_list'),
    path('class/users/upload/', views.UploadCvView.as_view(), name='ad_cv'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
