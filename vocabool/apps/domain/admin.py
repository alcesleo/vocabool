from django.contrib import admin
from vocabool.apps.domain.models import Vocabulary, Term, Clarification, Userterm

class TermAdmin(admin.ModelAdmin):
    list_display = ('text', 'language')
    search_fields = ('text',)

admin.site.register(Term, TermAdmin)


class UsertermAdmin(admin.ModelAdmin):
    list_display = ('term', 'vocabulary', 'created')
    list_filter = ('created',)
    search_fields = ('text',)
    ordering = ('-created',)

admin.site.register(Userterm, UsertermAdmin)

class ClarificationAdmin(admin.ModelAdmin):
    list_display = ('term', 'text', 'language', 'clarification_type', 'created')

admin.site.register(Clarification, ClarificationAdmin)

class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'owner', 'created')

admin.site.register(Vocabulary, VocabularyAdmin)
