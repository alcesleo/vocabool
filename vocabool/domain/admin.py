from django.contrib import admin
from vocabool.domain.models import Vocabulary, Term, Clarification, Listeme

class TermAdmin(admin.ModelAdmin):
    list_display = ('text', 'language')
    search_fields = ('text',)

admin.site.register(Term, TermAdmin)

class ListemeAdmin(admin.ModelAdmin):
    list_display = ('term', 'vocabulary', 'created')
    list_filter = ('created',)
    search_fields = ('text',)
    ordering = ('-created',)
    filter_horizontal = ('clarifications',)

admin.site.register(Listeme, ListemeAdmin)

class ClarificationAdmin(admin.ModelAdmin):
    list_display = ('text', 'term', 'language', 'category', 'created')
    ordering = ('term',)

admin.site.register(Clarification, ClarificationAdmin)

class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'owner', 'created')

admin.site.register(Vocabulary, VocabularyAdmin)
