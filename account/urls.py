from django.urls import path, include
from django.contrib.auth import views as auth_views
from account import views

urlpatterns = [
    # Add django authentication url patterns
    path('', include('django.contrib.auth.urls')),
    # Add user dashboard url pattern
    path('dashboard', views.dashboard, name='dashboard'),
    # Add user registration url pattern
    path('register/', views.register, name='register'),
    # Add user edit url pattern
    path('edit/', views.edit, name='edit'),
]
