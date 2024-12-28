"""
Views for the lettings application.

This module provides two main views:
- index: lists all lettings.
- letting: shows the details of a specific letting identified by its ID.
"""

import logging

from django.shortcuts import render, get_object_or_404
from .models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """
    Display a list of all available lettings.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The rendered 'lettings/index.html' template,
        populated with the queryset of all Letting objects.
    """
    lettings_list = Letting.objects.all()
    logger.debug("Index view called: found %d lettings", lettings_list.count())
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Display details for a specific letting.

    Args:
        request (HttpRequest): The incoming HTTP request.
        letting_id (int): The primary key of the Letting object to be retrieved.

    Returns:
        HttpResponse: The rendered 'lettings/letting.html' template,
        containing the title and address of the specified letting.
    """
    # Option 1 : get_object_or_404
    letting = get_object_or_404(Letting, id=letting_id)
    # On peut logger une info sur l'objet trouvé
    logger.info("Letting view called for letting_id=%s (title=%s)", letting_id, letting.title)

    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
