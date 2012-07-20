# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Location.lng'
        db.alter_column('openrov_location', 'lng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=11, decimal_places=8))

    def backwards(self, orm):

        # Changing field 'Location.lng'
        db.alter_column('openrov_location', 'lng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=8))

    models = {
        'openrov.location': {
            'Meta': {'ordering': "('-remote_date_created',)", 'object_name': 'Location'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '8'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '8'}),
            'remote_date_created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'remote_date_modified': ('django.db.models.fields.DateTimeField', [], {}),
            'remote_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'remote_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'openrov.video': {
            'Meta': {'ordering': "('video_id',)", 'object_name': 'Video'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['openrov.Location']"}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['openrov']