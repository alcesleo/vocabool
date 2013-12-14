from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.api import Api
from vocabool.domain.models import Vocabulary, Listeme, Clarification

# resources

class ClarificationResource(ModelResource):
    class Meta:
        queryset = Clarification.objects.all()
        resource_name = 'clarification'

class ListemeResource(ModelResource):
    clarifications = fields.ManyToManyField(ClarificationResource, 'clarifications',
                                            full=True)
    class Meta:
        queryset = Listeme.objects.all()
        resource_name = 'listeme'

class VocabularyResource(ModelResource):
    listeme = fields.ManyToManyField(ListemeResource, 'listemes',
                                     full_list=False,
                                     full_detail=True)
    class Meta:
        queryset = Vocabulary.objects.all()
        resource_name = 'vocabulary'
        # filtering = { 'title': tastypie.constants.ALL }


# register the api

v0 = Api(api_name='v0')
v0.register(VocabularyResource())
v0.register(ClarificationResource())
v0.register(ListemeResource())
