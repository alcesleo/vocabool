from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', lambda r: HttpResponseRedirect('/app/')),

    url(r'^users/', lambda r: HttpResponseRedirect('/app/')), # FIXME: ugly hack for login views
    url(r'^accounts/', include('vocabool.accounts.urls')),
    url(r'^app/', login_required(TemplateView.as_view(template_name='client/app.html'))),
    url(r'^api/', include('vocabool.api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
