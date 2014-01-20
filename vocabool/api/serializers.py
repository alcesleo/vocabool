from rest_framework import serializers
from django.contrib.auth.models import User
from vocabool.domain.models import Vocabulary, Term, Definition, Translation
from vocabool.libs.helpers import strip_on_last


class UserSerializer(serializers.ModelSerializer):
    vocabularies = serializers.HyperlinkedRelatedField(many=True, view_name='vocabularies')

    class Meta:
        model = User
        fields = ('id', 'username', 'vocabularies')


class DefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definition
        fields = ('definition', 'language')

    def transform_definition(self, obj, value):
        """Shorten long definition texts."""
        return strip_on_last('\n', value, 400)


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ('translation', 'to_language')


class TermSerializer(serializers.ModelSerializer):
    definitions = DefinitionSerializer(many=True, read_only=True)
    translations = TranslationSerializer(many=True, read_only=True)

    class Meta:
        model = Term
        fields = ('id', 'text', 'custom_text', 'language',
                  'definitions', 'translations', 'timestamp')


class VocabularySerializer(serializers.ModelSerializer):
    count = serializers.Field(source='count')

    class Meta:
        model = Vocabulary
        fields = ('id', 'name', 'count')
