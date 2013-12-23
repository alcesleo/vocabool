from rest_framework import serializers
from vocabool.domain.models import Vocabulary, Term
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    vocabularies = serializers.HyperlinkedRelatedField(many=True, view_name='vocabularies')

    class Meta:
        model = User
        fields = ('id', 'username', 'vocabularies')


class TermSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username') # username intsead of id
    class Meta:
        model = Term
        fields = ('text', 'custom_text', 'language', 'owner')


class VocabularySerializer(serializers.ModelSerializer):
    terms = TermSerializer(many=True)
    class Meta:
        model = Vocabulary

    def restore_fields(self, data, files):
        deserialized = super(VocabularySerializer, self).restore_fields(data, files)
        #TODO: whatever you feel like doing before it gets saved
        return deserialized
