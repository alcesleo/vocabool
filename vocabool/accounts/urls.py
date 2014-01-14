from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'', include('registration.backends.simple.urls')),
)
