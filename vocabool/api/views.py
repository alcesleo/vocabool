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

    def pre_save(self, obj):
        # set current user to owner
        obj.owner = self.request.user


    def get_queryset(self):
        # select only terms from vocabulary
        vocabulary = self.kwargs['pk'] # TODO: slugfield?
        return Term.objects.filter(vocabulary=vocabulary)


class TermDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Term
    serializer_class = TermSerializer
