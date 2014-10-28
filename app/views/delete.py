# import libraries
from django.contrib import messages
from django.views.generic.edit import DeleteView 

# import models
from app.models import BloodGroup
from app.models import Individual

class DeleteBloodGroup(DeleteView):
    """
    view for deleting bloodgroup
    """
    model = BloodGroup
    template_name = 'common/confirm_delete.html'
    success_url = '/app/bloodgroup'

    def get_context_data(self, **kwargs):
        context = super(DeleteBloodGroup, self).get_context_data(**kwargs)
        context['cancel_url'] = self.request.META["HTTP_REFERER"]
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Bloodgroup deleted successfully.')
        return super(DeleteBloodGroup, self).delete(request, *args, **kwargs)

class DeleteIndividual(DeleteView):
    """
    view for deleting individual
    """
    model = Individual
    template_name = 'common/confirm_delete.html'
    success_url = '/app/individual'

    def get_context_data(self, **kwargs):
        context = super(DeleteIndividual, self).get_context_data(**kwargs)
        context['cancel_url'] = self.request.META["HTTP_REFERER"]
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Individual deleted successfully.')
        return super(DeleteIndividual, self).delete(request, *args, **kwargs)


