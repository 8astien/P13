"""
Application configuration module for oc_lettings_site.

This module defines the OCLettingsSiteConfig class, which sets
the name and label for the oc_lettings_site application.
"""

from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """
    Configuration class for the oc_lettings_site application.

    Attributes:
        name (str): The full Python path to the application.
        label (str): A short, human-readable label for the application.
    """
    name = 'oc_lettings_site'
    label = 'oc_lettings_site'
