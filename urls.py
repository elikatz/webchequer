from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin
from scheduler.views import hello

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webchequer.views.home', name='home'),
    # url(r'^webchequer/', include('webchequer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #Scheduler Urls
    (r'^hello/$', hello),
)
