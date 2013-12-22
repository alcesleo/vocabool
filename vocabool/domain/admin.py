from django.contrib import admin
from vocabool.domain.models import Definition, Translation, Vocabulary, Term


class DefinitionAdmin(admin.ModelAdmin):
    list_display = ('text', 'definition')
    list_filter = ('timestamp', 'language')
    search_fields = ('text', 'definition')
    ordering = ('-timestamp',)


class TranslationAdmin(admin.ModelAdmin):
    list_display = ('text', 'translation', 'from_language', 'to_language')
    search_fields = ('text', 'translation')
    ordering = ('text',)


class TermInline(admin.TabularInline):
    model = Term

class TermAdmin(admin.ModelAdmin):
    list_display = ('text', 'custom_text', 'language', 'timestamp')
    search_fields = ('text', 'custom_text')

    filter_horizontal = ('definitions', 'translations')

class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'count', 'timestamp')
    search_fields = ('name',)
    inlines = [TermInline]



admin.site.register(Definition, DefinitionAdmin)
admin.site.register(Translation, TranslationAdmin)
admin.site.register(Vocabulary, VocabularyAdmin)
admin.site.register(Term, TermAdmin)
