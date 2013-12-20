from django.conf.urls import patterns, include, url
from vocabool.domain.api import v0 as v0_api
from vocabool.client.views import index

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'', index),
    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v0_api.urls)),
)
