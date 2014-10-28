from django.conf import settings
from django.views.generic.list import ListView

from app.models import BloodGroup
from app.models import Individual

from math import fabs

class ListBloodGroups(ListView):
    """generate list of bloodgroups"""
    model = BloodGroup
    paginate_by = settings.RECORDS_PER_PAGE
    template_name = "list/bloodgroup.html"

    def get_page(self):
        if self.request.GET.get('page', None) is not None:
            return int(self.request.GET.get('page'))
        else:            
            return 1

    def get_context_data(self, **kwargs):
        context = super(ListBloodGroups, self).get_context_data(**kwargs)
        current_page = self.get_page()
        paginator = context['paginator']
        page = paginator.page(current_page)
        context['result'] = page
        context['current_page'] = current_page
        context['total_pages'] =  paginator.num_pages
        context['page_range'] = [x for x in paginator.page_range if (fabs(x - current_page) <= settings.PAGINATION_LIMIT)]       
        context['has_next'] = page.has_next()
        context['has_previous'] = page.has_previous()
        if context['has_next'] == True:
            context['next_page'] = page.next_page_number()
        else:
            pass
        if context['has_previous'] == True:
            context['previous_page'] = page.previous_page_number()
        else:
            pass
        return context
 
class ListIndividuals(ListView):
    """generate list of individuals"""
    model = Individual
    paginate_by = settings.RECORDS_PER_PAGE
    template_name = "list/individual.html"

    def get_page(self):
        if self.request.GET.get('page', None) is not None:
            return int(self.request.GET.get('page'))
        else:            
            return 1

    def get_context_data(self, **kwargs):
        context = super(ListIndividuals, self).get_context_data(**kwargs)
        current_page = self.get_page()
        paginator = context['paginator']
        page = paginator.page(current_page)
        context['result'] = page
        context['current_page'] = current_page
        context['total_pages'] =  paginator.num_pages
        context['page_range'] = [x for x in paginator.page_range if (fabs(x - current_page) <= settings.PAGINATION_LIMIT)]       
        context['has_next'] = page.has_next()
        context['has_previous'] = page.has_previous()
        if context['has_next'] == True:
            context['next_page'] = page.next_page_number()
        else:
            pass
        if context['has_previous'] == True:
            context['previous_page'] = page.previous_page_number()
        else:
            pass
        return context
