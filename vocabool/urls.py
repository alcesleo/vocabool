from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),

    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include('vocabool.service.urls')),
)
