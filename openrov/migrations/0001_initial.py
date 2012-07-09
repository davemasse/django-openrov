# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table('openrov_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('remote_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('remote_text', self.gf('django.db.models.fields.TextField')(null=True)),
            ('remote_date_created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('remote_date_modified', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('video_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('lat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2)),
            ('lng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal('openrov', ['Location'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table('openrov_location')


    models = {
        'openrov.location': {
            'Meta': {'ordering': "('-remote_date_created',)", 'object_name': 'Location'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2'}),
            'remote_date_created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'remote_date_modified': ('django.db.models.fields.DateTimeField', [], {}),
            'remote_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'remote_text': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['openrov']