from tastypie import fields
from tastypie.resources import ModelResource
from vocabool.domain.models import Vocabulary, Listeme, Clarification



class ClarificationResource(ModelResource):
    class Meta:
        queryset = Clarification.objects.all()
        resource_name = 'clarification'

class ListemeResource(ModelResource):
    clarifications = fields.ManyToManyField(ClarificationResource, 'clarifications')
    class Meta:
        queryset = Listeme.objects.all()
        resource_name = 'listeme'

class VocabularyResource(ModelResource):
    listeme = fields.ManyToManyField(ListemeResource, 'listemes', full=True)
    class Meta:
        queryset = Vocabulary.objects.all()
        resource_name = 'vocabulary'
        # filtering = { 'title': tastypie.constants.ALL }
