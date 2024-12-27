"""
View functions for oc_lettings_site.

This module provides:
- The index view for the project's homepage.
"""

import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """
    Render the homepage of the site.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The rendered 'index.html' template for the site homepage.
    """
    logger.info("Homepage (index) of oc_lettings_site was requested.")
    return render(request, 'index.html')


def trigger_error(request):
    1 / 0
