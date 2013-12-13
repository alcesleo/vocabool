from django.contrib import admin
from vocabool.apps.domain.models import Vocabulary, Term, Clarification, UserTerm

# Register your models here.
admin.site.register(Vocabulary)
admin.site.register(Term)
admin.site.register(Clarification)
admin.site.register(UserTerm)
