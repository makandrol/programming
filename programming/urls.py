from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth.views import login


urlpatterns = patterns('',
    url(r'^$', login),
    url(r'^accounts/profile', 'teams.views.index'),
    url(r'^teams/', include('teams.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
