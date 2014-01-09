from django.conf.urls import patterns, include, url
from vocabool.api import views

urlpatterns = patterns('',
    url(r'auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'vocabulary/$', views.VocabularyList.as_view()),
    url(r'vocabulary/(?P<v_pk>[0-9]+)/$', views.VocabularyDetail.as_view()),
    url(r'vocabulary/(?P<v_pk>[0-9]+)/term/$', views.TermList.as_view()),
    url(r'vocabulary/(?P<v_pk>[0-9]+)/term/(?P<t_pk>[0-9]+)/$', views.TermDetail.as_view()),
)
