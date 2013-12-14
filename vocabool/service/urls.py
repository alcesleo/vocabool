from django.conf.urls import patterns, include, url
from tastypie.api import Api
from .resources import VocabularyResource

# Register the api
v0_api = Api(api_name='v0')
v0_api.register(VocabularyResource())

urlpatterns = patterns('',
    url(r'', include(v0_api.urls))
)
