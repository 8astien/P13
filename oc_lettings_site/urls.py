"""
URL configuration for oc_lettings_site.

This module defines the root URLs for the project, including:
- The homepage (index)
- The profiles application routes
- The lettings application routes
- The admin interface
"""

from django.contrib import admin
from django.urls import include, path
from .views import index


def trigger_error(request):
    1 / 0


urlpatterns = [
    path('sentry/', trigger_error),
    path('', index, name='index'),
    path('profiles/', include(('profiles.urls', 'profiles'))),
    path('lettings/', include(('lettings.urls', 'lettings'))),
    path('admin/', admin.site.urls),
]
