"""
URL configuration for the lettings application.

This module defines URL patterns for:
- Displaying a list of all lettings (index page).
- Viewing the details of a specific letting by its ID.
"""

from django.urls import path
from .views import index, letting

urlpatterns = [
    path('', index, name='index'),
    path('<int:letting_id>/', letting, name='letting')
]
