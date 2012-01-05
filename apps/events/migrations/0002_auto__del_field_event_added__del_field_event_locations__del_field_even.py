# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Event.added'
        db.delete_column('events_event', 'added')

        # Deleting field 'Event.locations'
        db.delete_column('events_event', 'locations')

        # Deleting field 'Event.teaser'
        db.delete_column('events_event', 'teaser')

        # Deleting field 'Event.user'
        db.delete_column('events_event', 'user_id')

        # Deleting field 'Event.active'
        db.delete_column('events_event', 'active')

        # Adding field 'Event.address'
        db.add_column('events_event', 'address', self.gf('django.db.models.fields.TextField')(default='', max_length=250, blank=True), keep_default=False)

        # Adding field 'Event.is_published'
        db.add_column('events_event', 'is_published', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Event.created_at'
        db.add_column('events_event', 'created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 1, 5, 10, 39, 13, 561660), blank=True), keep_default=False)

        # Changing field 'Event.description'
        db.alter_column('events_event', 'description', self.gf('django.db.models.fields.TextField')(default=''))


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Event.added'
        raise RuntimeError("Cannot reverse this migration. 'Event.added' and its values cannot be restored.")

        # Adding field 'Event.locations'
        db.add_column('events_event', 'locations', self.gf('django.db.models.fields.TextField')(default='', max_length=250, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Event.teaser'
        raise RuntimeError("Cannot reverse this migration. 'Event.teaser' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Event.user'
        raise RuntimeError("Cannot reverse this migration. 'Event.user' and its values cannot be restored.")

        # Adding field 'Event.active'
        db.add_column('events_event', 'active', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)

        # Deleting field 'Event.address'
        db.delete_column('events_event', 'address')

        # Deleting field 'Event.is_published'
        db.delete_column('events_event', 'is_published')

        # Deleting field 'Event.created_at'
        db.delete_column('events_event', 'created_at')

        # Changing field 'Event.description'
        db.alter_column('events_event', 'description', self.gf('django.db.models.fields.TextField')(null=True))


    models = {
        'events.event': {
            'Meta': {'ordering': "('-start',)", 'object_name': 'Event'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '250', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['events']
