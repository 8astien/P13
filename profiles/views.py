"""
Views for the profiles application.

This module provides:
- index: displays a list of all profiles.
- profile: displays details for a specific user profile by username.
"""

import logging
from django.shortcuts import render, get_object_or_404
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """
    Display a list of all user profiles.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered 'profiles/index.html' with a list of profiles.
    """
    profiles_list = Profile.objects.all()
    logger.debug("Profiles index called: found %d profiles", profiles_list.count())

    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Display details of a specific user profile identified by username.

    Args:
        request (HttpRequest): The incoming HTTP request.
        username (str): The username of the Profile's associated User.

    Returns:
        HttpResponse: Rendered 'profiles/profile.html' for the requested Profile.
    """
    logger.info("Profile view called for username=%s", username)

    profile_obj = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile_obj}
    return render(request, 'profiles/profile.html', context)
