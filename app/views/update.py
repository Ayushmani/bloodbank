# import libraries
from django.contrib import messages
from django.views.generic.edit import FormView 
from django.views.generic.edit import UpdateView

# import models
from app.models import BloodGroup
from app.models import Individual

# import forms
from app.forms import BloodGroupForm
from app.forms import IndividualForm

class UpdateBloodGroup(UpdateView):
    """
    view for updating an existing bloodgroup
    """
    form_class = BloodGroupForm
    model = BloodGroup
    success_url = "/app/bloodgroup"
    template_name = "create/bloodgroup.html"

    def form_valid(self, form):
        messages.success(self.request, 'Bloodgroup updated successfully.')
        return super(UpdateBloodGroup, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Invalid data, Please check the inputs.')
        return super(UpdateBloodGroup, self).form_invalid(form)

class UpdateIndividual(UpdateView):
    """
    view for updating an existing bloodgroup
    """
    form_class = IndividualForm
    model = Individual
    success_url = "/app/individual"
    template_name = "create/individual.html"

    def form_valid(self, form):
        messages.success(self.request, 'Individual updated successfully.')
        return super(UpdateIndividual, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Invalid data, Please check the inputs.')
        return super(UpdateIndividual, self).form_invalid(form)

