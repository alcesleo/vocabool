from rest_framework import serializers
from ..domain.models import Vocabulary

class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary

    def restore_fields(self, data, files):
        deserialized = super(VocabularySerializer, self).restore_fields(data, files)
        #TODO: whatever you feel like doing before it gets saved
        return deserialized
