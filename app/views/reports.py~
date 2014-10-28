# import libraries
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from django.views.generic import TemplateView
from django.views.generic.base import View

# import models
from app.models import Individual
from app.models import BloodGroup

class ReportBloodgroupPopulation(TemplateView):
    """show a 3d pie chart representing the bloodgroup population"""
    template_name = "reports/bloodgroup_population.html"

class DataBloodgroupPopulation(View):
    """prepare data for bloodgroup population report"""
    template_name = "reports/bloodgroup_population_json.html"

    def get(self,request,*args,**kwargs):
        response = Individual.objects.values('bloodgroup').annotate(count=Count('bloodgroup'))
        for entry in response:
            entry['bloodgroup'] = BloodGroup.objects.get(pk=entry['bloodgroup']).name
        return render(request, self.template_name, {'response': response})
