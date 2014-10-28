# import libraries
from django import forms
from django.forms import ModelForm

# import models
from app.models import Individual

class SearchForm(ModelForm):
    """
    form for create/update individual
    """
    class Meta:
        model = Individual
        fields = ['bloodgroup']
        widgets = {
            'bloodgroup': forms.Select(attrs = {
                        'autofocus': 'autofocus',
                        'class': 'form-control'
                    }),
        }

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields["bloodgroup"].empty_label = "-- Select --"
