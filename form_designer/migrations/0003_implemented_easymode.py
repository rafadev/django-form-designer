# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'FormDefinitionField.choice_values'
        db.delete_column('form_designer_formdefinitionfield', 'choice_values')

        # Deleting field 'FormDefinitionField.help_text'
        db.delete_column('form_designer_formdefinitionfield', 'help_text')

        # Deleting field 'FormDefinitionField.initial'
        db.delete_column('form_designer_formdefinitionfield', 'initial')

        # Deleting field 'FormDefinitionField.label'
        db.delete_column('form_designer_formdefinitionfield', 'label')

        # Deleting field 'FormDefinitionField.choice_labels'
        db.delete_column('form_designer_formdefinitionfield', 'choice_labels')

        # Adding field 'FormDefinitionField.label_nl-nl'
        db.add_column('form_designer_formdefinitionfield', 'label_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.label_nl-be'
        db.add_column('form_designer_formdefinitionfield', 'label_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.initial_nl-nl'
        db.add_column('form_designer_formdefinitionfield', 'initial_nl-nl', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.initial_nl-be'
        db.add_column('form_designer_formdefinitionfield', 'initial_nl-be', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.help_text_nl-nl'
        db.add_column('form_designer_formdefinitionfield', 'help_text_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.help_text_nl-be'
        db.add_column('form_designer_formdefinitionfield', 'help_text_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_values_nl-nl'
        db.add_column('form_designer_formdefinitionfield', 'choice_values_nl-nl', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_values_nl-be'
        db.add_column('form_designer_formdefinitionfield', 'choice_values_nl-be', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_labels_nl-nl'
        db.add_column('form_designer_formdefinitionfield', 'choice_labels_nl-nl', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_labels_nl-be'
        db.add_column('form_designer_formdefinitionfield', 'choice_labels_nl-be', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Deleting field 'FormDefinition.title'
        db.delete_column('form_designer_formdefinition', 'title')

        # Deleting field 'FormDefinition.mail_to'
        db.delete_column('form_designer_formdefinition', 'mail_to')

        # Deleting field 'FormDefinition.error_message'
        db.delete_column('form_designer_formdefinition', 'error_message')

        # Deleting field 'FormDefinition.mail_subject'
        db.delete_column('form_designer_formdefinition', 'mail_subject')

        # Deleting field 'FormDefinition.submit_label'
        db.delete_column('form_designer_formdefinition', 'submit_label')

        # Deleting field 'FormDefinition.message_template'
        db.delete_column('form_designer_formdefinition', 'message_template')

        # Deleting field 'FormDefinition.success_message'
        db.delete_column('form_designer_formdefinition', 'success_message')

        # Adding field 'FormDefinition.title_nl-nl'
        db.add_column('form_designer_formdefinition', 'title_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.title_nl-be'
        db.add_column('form_designer_formdefinition', 'title_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_to_nl-nl'
        db.add_column('form_designer_formdefinition', 'mail_to_nl-nl', self.gf('form_designer.fields.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_to_nl-be'
        db.add_column('form_designer_formdefinition', 'mail_to_nl-be', self.gf('form_designer.fields.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_subject_nl-nl'
        db.add_column('form_designer_formdefinition', 'mail_subject_nl-nl', self.gf('form_designer.fields.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_subject_nl-be'
        db.add_column('form_designer_formdefinition', 'mail_subject_nl-be', self.gf('form_designer.fields.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.success_message_nl-nl'
        db.add_column('form_designer_formdefinition', 'success_message_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.success_message_nl-be'
        db.add_column('form_designer_formdefinition', 'success_message_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.error_message_nl-nl'
        db.add_column('form_designer_formdefinition', 'error_message_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.error_message_nl-be'
        db.add_column('form_designer_formdefinition', 'error_message_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.submit_label_nl-nl'
        db.add_column('form_designer_formdefinition', 'submit_label_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.submit_label_nl-be'
        db.add_column('form_designer_formdefinition', 'submit_label_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.message_template_nl-nl'
        db.add_column('form_designer_formdefinition', 'message_template_nl-nl', self.gf('form_designer.fields.TemplateTextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.message_template_nl-be'
        db.add_column('form_designer_formdefinition', 'message_template_nl-be', self.gf('form_designer.fields.TemplateTextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'FormDefinitionField.choice_values'
        db.add_column('form_designer_formdefinitionfield', 'choice_values', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.help_text'
        db.add_column('form_designer_formdefinitionfield', 'help_text', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.initial'
        db.add_column('form_designer_formdefinitionfield', 'initial', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.label'
        db.add_column('form_designer_formdefinitionfield', 'label', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_labels'
        db.add_column('form_designer_formdefinitionfield', 'choice_labels', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Deleting field 'FormDefinitionField.label_nl-nl'
        db.delete_column('form_designer_formdefinitionfield', 'label_nl-nl')

        # Deleting field 'FormDefinitionField.label_nl-be'
        db.delete_column('form_designer_formdefinitionfield', 'label_nl-be')

        # Deleting field 'FormDefinitionField.initial_nl-nl'
        db.delete_column('form_designer_formdefinitionfield', 'initial_nl-nl')

        # Deleting field 'FormDefinitionField.initial_nl-be'
        db.delete_column('form_designer_formdefinitionfield', 'initial_nl-be')

        # Deleting field 'FormDefinitionField.help_text_nl-nl'
        db.delete_column('form_designer_formdefinitionfield', 'help_text_nl-nl')

        # Deleting field 'FormDefinitionField.help_text_nl-be'
        db.delete_column('form_designer_formdefinitionfield', 'help_text_nl-be')

        # Deleting field 'FormDefinitionField.choice_values_nl-nl'
        db.delete_column('form_designer_formdefinitionfield', 'choice_values_nl-nl')

        # Deleting field 'FormDefinitionField.choice_values_nl-be'
        db.delete_column('form_designer_formdefinitionfield', 'choice_values_nl-be')

        # Deleting field 'FormDefinitionField.choice_labels_nl-nl'
        db.delete_column('form_designer_formdefinitionfield', 'choice_labels_nl-nl')

        # Deleting field 'FormDefinitionField.choice_labels_nl-be'
        db.delete_column('form_designer_formdefinitionfield', 'choice_labels_nl-be')

        # Adding field 'FormDefinition.title'
        db.add_column('form_designer_formdefinition', 'title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_to'
        db.add_column('form_designer_formdefinition', 'mail_to', self.gf('form_designer.fields.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.error_message'
        db.add_column('form_designer_formdefinition', 'error_message', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_subject'
        db.add_column('form_designer_formdefinition', 'mail_subject', self.gf('form_designer.fields.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.submit_label'
        db.add_column('form_designer_formdefinition', 'submit_label', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.message_template'
        db.add_column('form_designer_formdefinition', 'message_template', self.gf('form_designer.fields.TemplateTextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.success_message'
        db.add_column('form_designer_formdefinition', 'success_message', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Deleting field 'FormDefinition.title_nl-nl'
        db.delete_column('form_designer_formdefinition', 'title_nl-nl')

        # Deleting field 'FormDefinition.title_nl-be'
        db.delete_column('form_designer_formdefinition', 'title_nl-be')

        # Deleting field 'FormDefinition.mail_to_nl-nl'
        db.delete_column('form_designer_formdefinition', 'mail_to_nl-nl')

        # Deleting field 'FormDefinition.mail_to_nl-be'
        db.delete_column('form_designer_formdefinition', 'mail_to_nl-be')

        # Deleting field 'FormDefinition.mail_subject_nl-nl'
        db.delete_column('form_designer_formdefinition', 'mail_subject_nl-nl')

        # Deleting field 'FormDefinition.mail_subject_nl-be'
        db.delete_column('form_designer_formdefinition', 'mail_subject_nl-be')

        # Deleting field 'FormDefinition.success_message_nl-nl'
        db.delete_column('form_designer_formdefinition', 'success_message_nl-nl')

        # Deleting field 'FormDefinition.success_message_nl-be'
        db.delete_column('form_designer_formdefinition', 'success_message_nl-be')

        # Deleting field 'FormDefinition.error_message_nl-nl'
        db.delete_column('form_designer_formdefinition', 'error_message_nl-nl')

        # Deleting field 'FormDefinition.error_message_nl-be'
        db.delete_column('form_designer_formdefinition', 'error_message_nl-be')

        # Deleting field 'FormDefinition.submit_label_nl-nl'
        db.delete_column('form_designer_formdefinition', 'submit_label_nl-nl')

        # Deleting field 'FormDefinition.submit_label_nl-be'
        db.delete_column('form_designer_formdefinition', 'submit_label_nl-be')

        # Deleting field 'FormDefinition.message_template_nl-nl'
        db.delete_column('form_designer_formdefinition', 'message_template_nl-nl')

        # Deleting field 'FormDefinition.message_template_nl-be'
        db.delete_column('form_designer_formdefinition', 'message_template_nl-be')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'publisher_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'form_designer.cmsformdefinition': {
            'Meta': {'object_name': 'CMSFormDefinition', 'db_table': "'cmsplugin_cmsformdefinition'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'form_definition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['form_designer.FormDefinition']"})
        },
        'form_designer.formdefinition': {
            'Meta': {'object_name': 'FormDefinition'},
            'action': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'allow_get_initial': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'error_message_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'form_template_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mail_from': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_nl-be': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_nl-nl': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_nl-be': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_nl-nl': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'message_template_nl-be': ('form_designer.fields.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_nl-nl': ('form_designer.fields.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'default': "'POST'", 'max_length': '10'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'submit_label_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_clear': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'success_message_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_redirect': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'form_designer.formdefinitionfield': {
            'Meta': {'ordering': "['position']", 'object_name': 'FormDefinitionField'},
            'choice_labels_nl-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_nl-nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_model': ('form_designer.fields.ModelNameField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'choice_model_empty_label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'choice_values_nl-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_nl-nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'decimal_places': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'field_class': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'form_definition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['form_designer.FormDefinition']"}),
            'help_text_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_result': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'initial_nl-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'initial_nl-nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'label_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'max_digits': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_length': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'min_length': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'regex': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'widget': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'form_designer.formlog': {
            'Meta': {'ordering': "['-created']", 'object_name': 'FormLog'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data': ('picklefield.fields.PickledObjectField', [], {'null': 'True', 'blank': 'True'}),
            'form_definition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['form_designer.FormDefinition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['form_designer']