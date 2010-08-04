# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'FormDefinitionField.label_nl-nl'
        db.add_column('form_designer_formdefinitionfield', 'label_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.label_nl-be'
        db.add_column('form_designer_formdefinitionfield', 'label_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.label_fr-be'
        db.add_column('form_designer_formdefinitionfield', 'label_fr-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.initial_nl-nl'
        db.add_column('form_designer_formdefinitionfield', 'initial_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.initial_nl-be'
        db.add_column('form_designer_formdefinitionfield', 'initial_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.initial_fr-be'
        db.add_column('form_designer_formdefinitionfield', 'initial_fr-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.help_text_nl-nl'
        db.add_column('form_designer_formdefinitionfield', 'help_text_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.help_text_nl-be'
        db.add_column('form_designer_formdefinitionfield', 'help_text_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.help_text_fr-be'
        db.add_column('form_designer_formdefinitionfield', 'help_text_fr-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_values_nl-nl'
        db.add_column('form_designer_formdefinitionfield', 'choice_values_nl-nl', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_values_nl-be'
        db.add_column('form_designer_formdefinitionfield', 'choice_values_nl-be', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_values_fr-be'
        db.add_column('form_designer_formdefinitionfield', 'choice_values_fr-be', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_labels_nl-nl'
        db.add_column('form_designer_formdefinitionfield', 'choice_labels_nl-nl', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_labels_nl-be'
        db.add_column('form_designer_formdefinitionfield', 'choice_labels_nl-be', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_labels_fr-be'
        db.add_column('form_designer_formdefinitionfield', 'choice_labels_fr-be', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.title_nl-nl'
        db.add_column('form_designer_formdefinition', 'title_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.title_nl-be'
        db.add_column('form_designer_formdefinition', 'title_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.title_fr-be'
        db.add_column('form_designer_formdefinition', 'title_fr-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_to_nl-nl'
        db.add_column('form_designer_formdefinition', 'mail_to_nl-nl', self.gf('form_designer.template_field.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_to_nl-be'
        db.add_column('form_designer_formdefinition', 'mail_to_nl-be', self.gf('form_designer.template_field.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_to_fr-be'
        db.add_column('form_designer_formdefinition', 'mail_to_fr-be', self.gf('form_designer.template_field.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_subject_nl-nl'
        db.add_column('form_designer_formdefinition', 'mail_subject_nl-nl', self.gf('form_designer.template_field.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_subject_nl-be'
        db.add_column('form_designer_formdefinition', 'mail_subject_nl-be', self.gf('form_designer.template_field.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_subject_fr-be'
        db.add_column('form_designer_formdefinition', 'mail_subject_fr-be', self.gf('form_designer.template_field.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.success_message_nl-nl'
        db.add_column('form_designer_formdefinition', 'success_message_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.success_message_nl-be'
        db.add_column('form_designer_formdefinition', 'success_message_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.success_message_fr-be'
        db.add_column('form_designer_formdefinition', 'success_message_fr-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.error_message_nl-nl'
        db.add_column('form_designer_formdefinition', 'error_message_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.error_message_nl-be'
        db.add_column('form_designer_formdefinition', 'error_message_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.error_message_fr-be'
        db.add_column('form_designer_formdefinition', 'error_message_fr-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.submit_label_nl-nl'
        db.add_column('form_designer_formdefinition', 'submit_label_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.submit_label_nl-be'
        db.add_column('form_designer_formdefinition', 'submit_label_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.submit_label_fr-be'
        db.add_column('form_designer_formdefinition', 'submit_label_fr-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.message_template_nl-nl'
        db.add_column('form_designer_formdefinition', 'message_template_nl-nl', self.gf('form_designer.template_field.TemplateTextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.message_template_nl-be'
        db.add_column('form_designer_formdefinition', 'message_template_nl-be', self.gf('form_designer.template_field.TemplateTextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.message_template_fr-be'
        db.add_column('form_designer_formdefinition', 'message_template_fr-be', self.gf('form_designer.template_field.TemplateTextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'FormDefinitionField.label_nl-nl'
        db.delete_column('form_designer_formdefinitionfield', 'label_nl-nl')

        # Deleting field 'FormDefinitionField.label_nl-be'
        db.delete_column('form_designer_formdefinitionfield', 'label_nl-be')

        # Deleting field 'FormDefinitionField.label_fr-be'
        db.delete_column('form_designer_formdefinitionfield', 'label_fr-be')

        # Deleting field 'FormDefinitionField.initial_nl-nl'
        db.delete_column('form_designer_formdefinitionfield', 'initial_nl-nl')

        # Deleting field 'FormDefinitionField.initial_nl-be'
        db.delete_column('form_designer_formdefinitionfield', 'initial_nl-be')

        # Deleting field 'FormDefinitionField.initial_fr-be'
        db.delete_column('form_designer_formdefinitionfield', 'initial_fr-be')

        # Deleting field 'FormDefinitionField.help_text_nl-nl'
        db.delete_column('form_designer_formdefinitionfield', 'help_text_nl-nl')

        # Deleting field 'FormDefinitionField.help_text_nl-be'
        db.delete_column('form_designer_formdefinitionfield', 'help_text_nl-be')

        # Deleting field 'FormDefinitionField.help_text_fr-be'
        db.delete_column('form_designer_formdefinitionfield', 'help_text_fr-be')

        # Deleting field 'FormDefinitionField.choice_values_nl-nl'
        db.delete_column('form_designer_formdefinitionfield', 'choice_values_nl-nl')

        # Deleting field 'FormDefinitionField.choice_values_nl-be'
        db.delete_column('form_designer_formdefinitionfield', 'choice_values_nl-be')

        # Deleting field 'FormDefinitionField.choice_values_fr-be'
        db.delete_column('form_designer_formdefinitionfield', 'choice_values_fr-be')

        # Deleting field 'FormDefinitionField.choice_labels_nl-nl'
        db.delete_column('form_designer_formdefinitionfield', 'choice_labels_nl-nl')

        # Deleting field 'FormDefinitionField.choice_labels_nl-be'
        db.delete_column('form_designer_formdefinitionfield', 'choice_labels_nl-be')

        # Deleting field 'FormDefinitionField.choice_labels_fr-be'
        db.delete_column('form_designer_formdefinitionfield', 'choice_labels_fr-be')

        # Deleting field 'FormDefinition.title_nl-nl'
        db.delete_column('form_designer_formdefinition', 'title_nl-nl')

        # Deleting field 'FormDefinition.title_nl-be'
        db.delete_column('form_designer_formdefinition', 'title_nl-be')

        # Deleting field 'FormDefinition.title_fr-be'
        db.delete_column('form_designer_formdefinition', 'title_fr-be')

        # Deleting field 'FormDefinition.mail_to_nl-nl'
        db.delete_column('form_designer_formdefinition', 'mail_to_nl-nl')

        # Deleting field 'FormDefinition.mail_to_nl-be'
        db.delete_column('form_designer_formdefinition', 'mail_to_nl-be')

        # Deleting field 'FormDefinition.mail_to_fr-be'
        db.delete_column('form_designer_formdefinition', 'mail_to_fr-be')

        # Deleting field 'FormDefinition.mail_subject_nl-nl'
        db.delete_column('form_designer_formdefinition', 'mail_subject_nl-nl')

        # Deleting field 'FormDefinition.mail_subject_nl-be'
        db.delete_column('form_designer_formdefinition', 'mail_subject_nl-be')

        # Deleting field 'FormDefinition.mail_subject_fr-be'
        db.delete_column('form_designer_formdefinition', 'mail_subject_fr-be')

        # Deleting field 'FormDefinition.success_message_nl-nl'
        db.delete_column('form_designer_formdefinition', 'success_message_nl-nl')

        # Deleting field 'FormDefinition.success_message_nl-be'
        db.delete_column('form_designer_formdefinition', 'success_message_nl-be')

        # Deleting field 'FormDefinition.success_message_fr-be'
        db.delete_column('form_designer_formdefinition', 'success_message_fr-be')

        # Deleting field 'FormDefinition.error_message_nl-nl'
        db.delete_column('form_designer_formdefinition', 'error_message_nl-nl')

        # Deleting field 'FormDefinition.error_message_nl-be'
        db.delete_column('form_designer_formdefinition', 'error_message_nl-be')

        # Deleting field 'FormDefinition.error_message_fr-be'
        db.delete_column('form_designer_formdefinition', 'error_message_fr-be')

        # Deleting field 'FormDefinition.submit_label_nl-nl'
        db.delete_column('form_designer_formdefinition', 'submit_label_nl-nl')

        # Deleting field 'FormDefinition.submit_label_nl-be'
        db.delete_column('form_designer_formdefinition', 'submit_label_nl-be')

        # Deleting field 'FormDefinition.submit_label_fr-be'
        db.delete_column('form_designer_formdefinition', 'submit_label_fr-be')

        # Deleting field 'FormDefinition.message_template_nl-nl'
        db.delete_column('form_designer_formdefinition', 'message_template_nl-nl')

        # Deleting field 'FormDefinition.message_template_nl-be'
        db.delete_column('form_designer_formdefinition', 'message_template_nl-be')

        # Deleting field 'FormDefinition.message_template_fr-be'
        db.delete_column('form_designer_formdefinition', 'message_template_fr-be')


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
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True', 'blank': 'True'}),
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
            'allow_get_initial': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'error_message_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'form_template_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_data': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'mail_from': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_en': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_fr-be': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_nl': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_nl-be': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_nl-nl': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_en': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_fr-be': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_nl': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_nl-be': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_nl-nl': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'message_template_en': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_fr-be': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_nl': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_nl-be': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_nl-nl': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'default': "'POST'", 'max_length': '10'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'submit_label_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_clear': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'success_message_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_redirect': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'form_designer.formdefinitionfield': {
            'Meta': {'object_name': 'FormDefinitionField'},
            'choice_labels_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_fr-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_nl-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_nl-nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_model': ('form_designer.model_name_field.ModelNameField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'choice_model_empty_label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'choice_values_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_fr-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_nl-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_nl-nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'decimal_places': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'field_class': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'form_definition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['form_designer.FormDefinition']"}),
            'help_text_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_result': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'initial_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
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
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'widget': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'form_designer.formlog': {
            'Meta': {'object_name': 'FormLog'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data': ('form_designer.pickled_object_field.PickledObjectField', [], {'null': 'True', 'blank': 'True'}),
            'form_definition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['form_designer.FormDefinition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['form_designer']
