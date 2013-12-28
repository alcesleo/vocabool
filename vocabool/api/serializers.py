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
        fields = ('text', 'custom_text', 'language', 'vocabulary', 'owner')


class VocabularySerializer(serializers.ModelSerializer):
    # terms = TermSerializer(many=True) only in detail
    owner = serializers.Field(source='owner.username') # username intsead of id
    count = serializers.Field(source='count')
    class Meta:
        model = Vocabulary
        fields = ('name', 'count', 'owner')
