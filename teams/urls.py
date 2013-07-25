from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import DetailView
from teams.models import Specification, Job

admin.autodiscover()
urlpatterns = patterns('',
                       url(r'^$', 'teams.views.index'),
                       url(r'^index$', 'teams.views.index'),
                       url(r'^customer$', 'teams.views.customer'),
                       url(r'^manager$', 'teams.views.manager'),
                       url(r'^developer$', 'teams.views.developer'),
                       url(r'^create_project$', 'teams.views.create_project'),
                       url(r'^create_project_form$', 'teams.views.create_project_form'),
                       url(r'^create_specification$', 'teams.views.create_specification'),
                       url(r'^create_specification_form$', 'teams.views.create_specification_form'),
                       url(r'^create_job$', 'teams.views.create_job'),
                       url(r'^create_job_form$', 'teams.views.create_job_form'),
                       url(r'^specification(?P<pk>\d+)$', 'teams.views.specification_detail'),
                       url(r'^job(?P<pk>\d+)$', 'teams.views.job_detail'),
                       url(r'^project(?P<pk>\d+)$', 'teams.views.project_detail'),
                       url(r'^choose$', 'teams.views.choose'),
                       url(r'^error$', 'teams.views.error'),
                       )

