# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SubmissionSet'
        db.create_table('sa_api_submissionset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(related_name='submission_sets', to=orm['sa_api_v2.Place'])),
            ('submission_type', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('sa_api_v2', ['SubmissionSet'])

        # Adding model 'Submission'
        db.create_table('sa_api_submission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('submitter_name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('data', self.gf('django.db.models.fields.TextField')(default='{}')),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='children', to=orm['sa_api_v2.SubmissionSet'])),
        ))
        db.send_create_signal('sa_api_v2', ['Submission'])


    def backwards(self, orm):
        # Deleting model 'SubmissionSet'
        db.delete_table('sa_api_submissionset')

        # Deleting model 'Submission'
        db.delete_table('sa_api_submission')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sa_api_v2.activity': {
            'Meta': {'object_name': 'Activity', 'db_table': "'sa_api_activity'"},
            'action': ('django.db.models.fields.CharField', [], {'default': "'create'", 'max_length': '16'}),
            'created_datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'data_object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'sa_api_v2.place': {
            'Meta': {'object_name': 'Place', 'db_table': "'sa_api_place'"},
            'created_datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'submitter_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'updated_datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'sa_api_v2.submission': {
            'Meta': {'object_name': 'Submission', 'db_table': "'sa_api_submission'"},
            'created_datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'to': "orm['sa_api_v2.SubmissionSet']"}),
            'submitter_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'updated_datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'sa_api_v2.submissionset': {
            'Meta': {'object_name': 'SubmissionSet', 'db_table': "'sa_api_submissionset'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'submission_sets'", 'to': "orm['sa_api_v2.Place']"}),
            'submission_type': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['sa_api_v2']