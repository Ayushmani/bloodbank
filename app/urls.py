# import libraries
from django.conf.urls import patterns, include, url

# import views
from views import ListBloodGroups
from views import ListIndividuals
from views import CreateBloodGroup
from views import CreateIndividual
from views import UpdateBloodGroup
from views import UpdateIndividual
from views import DeleteBloodGroup
from views import DeleteIndividual
from views import SearchIndividual
from views import ReportBloodgroupPopulation
from views import DataBloodgroupPopulation
from views import ApiListBloodGroup
from views import ApiUpdateDeleteBloodGroup

urlpatterns = patterns('',
    # list 
    url(r'^bloodgroup$', ListBloodGroups.as_view(), name='list_bloodgroup'),
    url(r'^individual$', ListIndividuals.as_view(), name='list_individual'),
    # create
    url(r'^bloodgroup/create$', CreateBloodGroup.as_view(), name='create_bloodgroup'),
    url(r'^individual/create$', CreateIndividual.as_view(), name='create_individual'),
    # update
    url(r'^bloodgroup/update/(?P<pk>\d{1,50})$', UpdateBloodGroup.as_view(), name='update_bloodgroup'),
    url(r'^individual/update/(?P<pk>\d{1,50})$', UpdateIndividual.as_view(), name='update_individual'),
    # delete
    url(r'^bloodgroup/delete/(?P<pk>\d{1,50})$', DeleteBloodGroup.as_view(), name='delete_bloodgroup'),
    url(r'^individual/delete/(?P<pk>\d{1,50})$', DeleteIndividual.as_view(), name='delete_individual'),
    # search
    url(r'^individual/search$', SearchIndividual.as_view(), name='search_individual'),
    # reports
    url(r'^reports/bloodgroup-population$', ReportBloodgroupPopulation.as_view(), name='report_bloodgroup_population'),
    # data
    url(r'^data/bloodgroup-population$', DataBloodgroupPopulation.as_view(), name='data_bloodgroup_population'),
    # api
    url(r'^api/bloodgroup$', ApiListBloodGroup.as_view(), name='api_list_bloodgroup'),
    url(r'^api/bloodgroup/(?P<pk>\d{1,50})$', ApiUpdateDeleteBloodGroup.as_view(), name='api_update_delete_bloodgroup'),
)
