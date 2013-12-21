from django.conf.urls import patterns, include, url
from .views import VocabularyView

urlpatterns = patterns('',
    url(r'^vocabularies/', VocabularyView.as_view(), name='vocabularies'),
)
