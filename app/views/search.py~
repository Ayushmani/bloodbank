# import libraries
from math import fabs
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic.edit import FormView

# import models
from app.models import Individual
from app.models import BloodGroup

# import forms
from app.forms import SearchForm

class SearchIndividual(FormView):
    """search individuals based on bloodgroup"""
    form_class = SearchForm
    success_url = "/app/individual/search"
    template_name = "search/individual.html"

    def fix_search_session(self):
        if self.request.GET.get('clear', None) is not None:
            if self.request.session.get('bloodgroup_id', None) is not None:
                del self.request.session['bloodgroup_id']
            else:
                pass
        else:
            pass

    def get_page(self):
        if self.request.GET.get('page', None) is not None:
            return int(self.request.GET.get('page'))
        else:            
            return 1

    def paginate_result(self, result, **kwargs):
        paginator = Paginator(result, settings.RECORDS_PER_PAGE)
        current_page = self.get_page()
        page = paginator.page(current_page)
        context = super(SearchIndividual, self).get_context_data(**kwargs)
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

    def get_context_data(self, **kwargs):
        self.fix_search_session()
        if self.request.session.get('bloodgroup_id', None) is not None:
            result = Individual.objects.filter(bloodgroup_id__exact = self.request.session['bloodgroup_id'])
        else:
            result = Individual.objects.all()
        context = self.paginate_result(result, **kwargs)
        return context

    def form_valid(self, form):
        self.request.session['bloodgroup_id'] = form.cleaned_data['bloodgroup'].id
        return super(SearchIndividual, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Invalid data, Please check the inputs.')
        return super(SearchIndividual, self).form_invalid(form)
