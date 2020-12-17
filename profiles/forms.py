from django import forms
from localflavor.us.forms import USStateSelect, USZipCodeField
from .models import UserProfile
 

class UserProfileForm(forms.ModelForm):
    defaultship_zipcode = USZipCodeField()
    """ Widget code from Nafees Anwar on stackoverflow 4/30/19 """
    defaultship_state = forms.CharField(widget=USStateSelect)

    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'defaultship_full_name': 'Full Name',
            'defaultship_phone_number': 'Phone',
            'defaultship_comp_name': 'Organization',
            'defaultship_street_address1': 'Street Address',
            'defaultship_street_address2': 'Apt/Suite/Floor',
            'defaultship_city': 'City',
            'defaultship_state': 'State',
            'defaultship_zipcode': 'Zip Code',
        }

        self.fields['defaultship_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'input-border profile-form-input'
            self.fields[field].label = False
