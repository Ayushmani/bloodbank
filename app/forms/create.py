# import libraries
from django import forms
from django.forms import ModelForm

# import models
from app.models import BloodGroup
from app.models import Individual

class BloodGroupForm(ModelForm):
    """
    form for create/update bloodgroup
    """
    class Meta:
        model = BloodGroup
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs = {
                        'autofocus': 'autofocus',
                        'placeholder': 'Enter name of the bloodgroup',
                        'class': 'form-control'
                    }),
            'description': forms.TextInput(attrs = {
                        'placeholder': 'Enter a small description',
                        'class': 'form-control'
                    }),
        }

class IndividualForm(ModelForm):
    """
    form for create/update individual
    """
    class Meta:
        model = Individual
        fields = ['bloodgroup', 'name', 'phone_number']
        widgets = {
            'bloodgroup': forms.Select(attrs = {
                        'autofocus': 'autofocus',
                        'class': 'form-control'
                    }),
            'name': forms.TextInput(attrs = {
                        'placeholder': 'Enter name of the individual',
                        'class': 'form-control'
                    }),
            'phone_number': forms.TextInput(attrs = {
                        'placeholder': 'Enter phone number of the individual',
                        'class': 'form-control'
                    }),
        }

    def __init__(self, *args, **kwargs):
        super(IndividualForm, self).__init__(*args, **kwargs)
        self.fields["bloodgroup"].empty_label = "-- Select --"
