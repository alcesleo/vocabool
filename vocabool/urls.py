from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('vocabool.api.urls')),

    # route to the backbone app
    url(r'^$', lambda r: HttpResponseRedirect('app/')),
    url(r'^app/', TemplateView.as_view(template_name='client/index.html')),
)
