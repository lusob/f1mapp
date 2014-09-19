from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
#
urlpatterns = patterns('',
                       url(r'^$', 'f1mapp.views.home', name='home'),
                       url(r'^info$', 'f1mapp.views.info', name='info'),
                       url(r'^error$', 'f1mapp.views.error', name='error'),
                       url(r'^test$', 'f1mapp.views.test', name='test'),
                       url(r'^data$', 'f1mapp.views.data', name='data'),
                       url(r'^mapeditor$', 'f1mapp.views.mapeditor', name='mapeditor'),
                       )
