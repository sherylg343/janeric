from __future__ import unicode_literals

import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import CharField, Field, RegexField, Select
from django.utils.translation import ugettext_lazy as _

from django import forms
from localflavor.us.forms import USStateSelect, USZipCodeField
from .models import Order


class USStateSelect(Select):
    """A Select widget that uses a list of U.S. states/territories as its choices."""

    def __init__(self, attrs=None):
        from .us_states import STATE_CHOICES
        super(USStateSelect, self).__init__(attrs, choices=STATE_CHOICES)


class USZipCodeField(RegexField):
    """
    A form field that validates input as a U.S. ZIP code.

    Valid formats are XXXXX or XXXXX-XXXX.

    Whitespace around the ZIP code is accepted and automatically trimmed.
    """

    default_error_messages = {
        'invalid': _('Enter a zip code in the format XXXXX or XXXXX-XXXX.'),
    }

    def __init__(self, *args, **kwargs):
        super(USZipCodeField, self).__init__(r'^\d{5}(?:-\d{4})?$', *args, **kwargs)

    def to_python(self, value):
        value = super(USZipCodeField, self).to_python(value)
        if value in self.empty_values:
            return self.empty_value
        return value.strip()


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'city', 'state', 'zipcode',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated labels and set autofocus on first field
        """
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'city': 'City',
            'state': 'State',
            'zipcode': 'Zip Code',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'stripe-style-input'
        self.fields[field].label = False
