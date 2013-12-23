from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from vocabool.domain.models import Vocabulary, Term
from .serializers import VocabularySerializer, TermSerializer, UserSerializer
from .permissions import IsOwnerOrStaff


class VocabularyList(generics.ListCreateAPIView):
    model = Vocabulary
    serializer_class = VocabularySerializer
    permission_classes = (IsOwnerOrStaff,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class VocabularyDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Vocabulary
    serializer_class = VocabularySerializer
    permission_classes = (IsOwnerOrStaff,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class TermList(generics.ListCreateAPIView):
    model = Term
    serializer_class = TermSerializer


class TermDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Term
    serializer_class = TermSerializer
