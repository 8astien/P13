"""
Models for the profiles application.

This module defines the Profile model, which extends Django's User model
to include additional profile-related information such as a favorite city.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user profile in the system.

    Attributes:
        user (User): The User object linked via a one-to-one relationship.
        favorite_city (str): An optional field representing the user's favorite city.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Return a string representation of the profile, which is the username
        of the associated User.

        Returns:
            str: The username of the associated User.
        """
        return self.user.username
