# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Definition'
        db.create_table(u'domain_definition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('vocabool.domain.fields.LanguageField')(max_length=2)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('definition', self.gf('django.db.models.fields.TextField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'domain', ['Definition'])

        # Adding model 'Translation'
        db.create_table(u'domain_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_language', self.gf('vocabool.domain.fields.LanguageField')(max_length=2)),
            ('to_language', self.gf('vocabool.domain.fields.LanguageField')(max_length=2)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('translation', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'domain', ['Translation'])

        # Adding model 'Vocabulary'
        db.create_table(u'domain_vocabulary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='vocabularies', to=orm['auth.User'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'domain', ['Vocabulary'])

        # Adding model 'Term'
        db.create_table(u'domain_term', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='terms', to=orm['auth.User'])),
            ('vocabulary', self.gf('django.db.models.fields.related.ForeignKey')(related_name='terms', to=orm['domain.Vocabulary'])),
            ('language', self.gf('vocabool.domain.fields.LanguageField')(max_length=2)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('custom_text', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'domain', ['Term'])

        # Adding unique constraint on 'Term', fields ['text', 'language', 'vocabulary']
        db.create_unique(u'domain_term', ['text', 'language', 'vocabulary_id'])

        # Adding M2M table for field definitions on 'Term'
        m2m_table_name = db.shorten_name(u'domain_term_definitions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('term', models.ForeignKey(orm[u'domain.term'], null=False)),
            ('definition', models.ForeignKey(orm[u'domain.definition'], null=False))
        ))
        db.create_unique(m2m_table_name, ['term_id', 'definition_id'])

        # Adding M2M table for field translations on 'Term'
        m2m_table_name = db.shorten_name(u'domain_term_translations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('term', models.ForeignKey(orm[u'domain.term'], null=False)),
            ('translation', models.ForeignKey(orm[u'domain.translation'], null=False))
        ))
        db.create_unique(m2m_table_name, ['term_id', 'translation_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Term', fields ['text', 'language', 'vocabulary']
        db.delete_unique(u'domain_term', ['text', 'language', 'vocabulary_id'])

        # Deleting model 'Definition'
        db.delete_table(u'domain_definition')

        # Deleting model 'Translation'
        db.delete_table(u'domain_translation')

        # Deleting model 'Vocabulary'
        db.delete_table(u'domain_vocabulary')

        # Deleting model 'Term'
        db.delete_table(u'domain_term')

        # Removing M2M table for field definitions on 'Term'
        db.delete_table(db.shorten_name(u'domain_term_definitions'))

        # Removing M2M table for field translations on 'Term'
        db.delete_table(db.shorten_name(u'domain_term_translations'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'domain.definition': {
            'Meta': {'object_name': 'Definition'},
            'definition': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('vocabool.domain.fields.LanguageField', [], {'max_length': '2'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'domain.term': {
            'Meta': {'unique_together': "(('text', 'language', 'vocabulary'),)", 'object_name': 'Term'},
            'custom_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'definitions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'terms'", 'blank': 'True', 'to': u"orm['domain.Definition']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('vocabool.domain.fields.LanguageField', [], {'max_length': '2'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'terms'", 'to': u"orm['auth.User']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'translations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'terms'", 'blank': 'True', 'to': u"orm['domain.Translation']"}),
            'vocabulary': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'terms'", 'to': u"orm['domain.Vocabulary']"})
        },
        u'domain.translation': {
            'Meta': {'object_name': 'Translation'},
            'from_language': ('vocabool.domain.fields.LanguageField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'to_language': ('vocabool.domain.fields.LanguageField', [], {'max_length': '2'}),
            'translation': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'domain.vocabulary': {
            'Meta': {'object_name': 'Vocabulary'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vocabularies'", 'to': u"orm['auth.User']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['domain']