from django.contrib.auth.models import User
from rest_framework import permissions, exceptions, generics, filters
from .serializers import VocabularySerializer, TermSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from vocabool.domain.models import Vocabulary, Term, Definition
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
        raise exceptions.NotAuthenticated()


class VocabularyDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Vocabulary
    serializer_class = VocabularySerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class TermList(generics.ListCreateAPIView):
    """
    Lists terms in a specific vocabulary (from query-string).
    Owner has full permissions, everyone has read premissions.
    Handles ?ordering= in query-string.
    """

    model = Term
    serializer_class = TermSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    # enable ?ordering=
    filter_backends = (filters.OrderingFilter,)
    ordering = ('text', 'timestamp')


    def pre_save(self, obj):
        obj.owner = self.request.user
        obj.vocabulary_id = self.kwargs['pk'] # TODO: if not exists


    def get_queryset(self):
        # select only terms from vocabulary
        vocabulary = self.kwargs['pk']
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
    permission_classes = (IsOwnerOrReadOnly,)


    def _handle_query(self, term, params):
        """Calls service methods on object based on GET-parameters."""
        service = Service()

        if 'define' in params:
            service.define(term)

        if 'translate_to' in params:
            service.translate(term, params['translate_to'])

    # handle query params
    def get_object(self):

        # get the object normally
        term = super(TermDetail, self).get_object()
        # TODO handle not found, get object or 404?

        # attatch definitions and translations if requested
        self._handle_query(term, self.request.QUERY_PARAMS)

        return term
