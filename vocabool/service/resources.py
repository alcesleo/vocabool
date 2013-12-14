from tastypie import fields
from tastypie.resources import ModelResource
from vocabool.domain.models import Vocabulary, Listeme

class ListemeResource(ModelResource):
    class Meta:
        queryset = Listeme.objects.all()
        resource_name = 'listeme'

class VocabularyResource(ModelResource):
    listeme = fields.ToManyField(ListemeResource, 'listemes', full_list=False, full_detail=True)
    class Meta:
        queryset = Vocabulary.objects.all()
        resource_name = 'vocabulary'
