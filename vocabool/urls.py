from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('vocabool.api.urls')),
    # all other matches gets the index
    url(r'', TemplateView.as_view(template_name='client/index.html')),
)
