from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
#
urlpatterns = patterns('',
    url(r'^$', 'f1mapp.views.home', name='home'),
    url(r'^info$', 'f1mapp.views.info', name='info'),
)
