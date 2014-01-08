from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^users/', lambda r: HttpResponseRedirect('/app/')), # FIXME: ugly hack for login views
    url(r'', include('registration.backends.simple.urls')),
)
