"""
This module defines models related to property lettings.

It contains the Address and Letting models, which store information
about a property's location and its corresponding letting.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a physical address.

    Attributes:
        number (int): The street number, validated to be at most 9999.
        street (str): The street name, with a maximum length of 64 characters.
        city (str): The city name, with a maximum length of 64 characters.
        state (str): A two-character state code, validated to have at least 2 chars.
        zip_code (int): The ZIP or postal code, validated to be at most 99999.
        country_iso_code (str): A three-character country ISO code, validated
            to have at least 3 chars.
    """

    class Meta:
        verbose_name_plural = 'addresses'

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Return a string representation of the address, typically used in admin lists
        and debugging.

        Returns:
            str: The street address in "number street" format.
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Represents a letting, linking a title to an Address.

    Attributes:
        title (str): A descriptive title for the letting (e.g., property name).
        address (Address): A one-to-one relation to an Address object.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a string representation of the letting.

        Returns:
            str: The letting title.
        """
        return self.title
