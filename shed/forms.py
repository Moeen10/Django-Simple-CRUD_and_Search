from django import forms
from .models import Shed_registration

class ShedForm(forms.ModelForm):
    class Meta:
        model = Shed_registration
        fields = ['shedName', 'shedLength', 'shedWidth', 'shedLocation', 'phoneNumber','email','number_of_cow']