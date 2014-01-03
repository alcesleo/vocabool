from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from vocabool.domain.models import Vocabulary, Term, Definition
from .serializers import VocabularySerializer, TermSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from vocabool.webservices.service import Service


class VocabularyList(generics.ListCreateAPIView):
    model = Vocabulary
    serializer_class = VocabularySerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


    def get_queryset(self):
        # get only owned vocabularies
        user = self.request.user
        if user.is_authenticated():
            return Vocabulary.objects.filter(owner=user)
        return Vocabulary.objects.all() # TODO: When logged out?


class VocabularyDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Vocabulary
    serializer_class = VocabularySerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class TermList(generics.ListCreateAPIView):
    model = Term
    serializer_class = TermSerializer


    def pre_save(self, obj):
        obj.owner = self.request.user

        # TODO: set vocabulary here


    def get_queryset(self):
        # select only terms from vocabulary
        vocabulary = self.kwargs['pk'] # TODO: slugfield?
        return Term.objects.filter(vocabulary=vocabulary)


class TermDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    On top of handling the normal operations on specific Term object,
    this class handles some query params.

    GET-parameters:
        ?define           -- add a definition object before returning
        ?translate_to=en  -- add a translation (here to english) object before returning

    These can be used together:

        /api/term/3/?translate_to=ru&define

    """

    model = Term
    serializer_class = TermSerializer


    def _handle_query(self, term, params):
        """Calls service methods on object based on GET-parameters."""

        # TODO: DOCUMENT QUERY PARAMS!!!!!
        # TODO: instanciate when needed or static service?
        service = Service()

        if 'define' in params:
            service.define(term)


        if 'translate_to' in params:
            service.translate(term, params['translate_to'])

    # handle query params
    def get_object(self):

        # get the object normally
        term = super(TermDetail, self).get_object()
        # TODO handle not found

        # attatch definitions and translations if requested
        self._handle_query(term, self.request.QUERY_PARAMS)

        return term
