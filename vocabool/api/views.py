from rest_framework import generics
from ..domain.models import Vocabulary
from .serializers import VocabularySerializer


class VocabularyView(generics.ListCreateAPIView):
    model = Vocabulary
    serializer_class = VocabularySerializer


class VocabularyDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = Vocabulary
    serializer_class = VocabularySerializer
