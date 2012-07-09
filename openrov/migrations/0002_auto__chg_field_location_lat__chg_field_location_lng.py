# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Location.lat'
        db.alter_column('openrov_location', 'lat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=8))

        # Changing field 'Location.lng'
        db.alter_column('openrov_location', 'lng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=8))

    def backwards(self, orm):

        # Changing field 'Location.lat'
        db.alter_column('openrov_location', 'lat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'Location.lng'
        db.alter_column('openrov_location', 'lng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

    models = {
        'openrov.location': {
            'Meta': {'ordering': "('-remote_date_created',)", 'object_name': 'Location'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '8'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '8'}),
            'remote_date_created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'remote_date_modified': ('django.db.models.fields.DateTimeField', [], {}),
            'remote_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'remote_text': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['openrov']