"""
URL configuration for the profiles application.

This module defines URL patterns for:
- Displaying a list of all user profiles.
- Viewing details of a specific profile by username.
"""

from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
