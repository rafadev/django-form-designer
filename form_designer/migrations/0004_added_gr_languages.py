# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'FormDefinitionField.label_it-it'
        db.add_column('form_designer_formdefinitionfield', 'label_it-it', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.label_es-es'
        db.add_column('form_designer_formdefinitionfield', 'label_es-es', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.initial_it-it'
        db.add_column('form_designer_formdefinitionfield', 'initial_it-it', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.initial_es-es'
        db.add_column('form_designer_formdefinitionfield', 'initial_es-es', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.help_text_it-it'
        db.add_column('form_designer_formdefinitionfield', 'help_text_it-it', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.help_text_es-es'
        db.add_column('form_designer_formdefinitionfield', 'help_text_es-es', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_values_it-it'
        db.add_column('form_designer_formdefinitionfield', 'choice_values_it-it', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_values_es-es'
        db.add_column('form_designer_formdefinitionfield', 'choice_values_es-es', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_labels_it-it'
        db.add_column('form_designer_formdefinitionfield', 'choice_labels_it-it', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_labels_es-es'
        db.add_column('form_designer_formdefinitionfield', 'choice_labels_es-es', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.title_it-it'
        db.add_column('form_designer_formdefinition', 'title_it-it', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.title_es-es'
        db.add_column('form_designer_formdefinition', 'title_es-es', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_to_it-it'
        db.add_column('form_designer_formdefinition', 'mail_to_it-it', self.gf('form_designer.template_field.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_to_es-es'
        db.add_column('form_designer_formdefinition', 'mail_to_es-es', self.gf('form_designer.template_field.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_subject_it-it'
        db.add_column('form_designer_formdefinition', 'mail_subject_it-it', self.gf('form_designer.template_field.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_subject_es-es'
        db.add_column('form_designer_formdefinition', 'mail_subject_es-es', self.gf('form_designer.template_field.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.success_message_it-it'
        db.add_column('form_designer_formdefinition', 'success_message_it-it', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.success_message_es-es'
        db.add_column('form_designer_formdefinition', 'success_message_es-es', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.error_message_it-it'
        db.add_column('form_designer_formdefinition', 'error_message_it-it', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.error_message_es-es'
        db.add_column('form_designer_formdefinition', 'error_message_es-es', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.submit_label_it-it'
        db.add_column('form_designer_formdefinition', 'submit_label_it-it', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.submit_label_es-es'
        db.add_column('form_designer_formdefinition', 'submit_label_es-es', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.message_template_it-it'
        db.add_column('form_designer_formdefinition', 'message_template_it-it', self.gf('form_designer.template_field.TemplateTextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.message_template_es-es'
        db.add_column('form_designer_formdefinition', 'message_template_es-es', self.gf('form_designer.template_field.TemplateTextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'FormDefinitionField.label_it-it'
        db.delete_column('form_designer_formdefinitionfield', 'label_it-it')

        # Deleting field 'FormDefinitionField.label_es-es'
        db.delete_column('form_designer_formdefinitionfield', 'label_es-es')

        # Deleting field 'FormDefinitionField.initial_it-it'
        db.delete_column('form_designer_formdefinitionfield', 'initial_it-it')

        # Deleting field 'FormDefinitionField.initial_es-es'
        db.delete_column('form_designer_formdefinitionfield', 'initial_es-es')

        # Deleting field 'FormDefinitionField.help_text_it-it'
        db.delete_column('form_designer_formdefinitionfield', 'help_text_it-it')

        # Deleting field 'FormDefinitionField.help_text_es-es'
        db.delete_column('form_designer_formdefinitionfield', 'help_text_es-es')

        # Deleting field 'FormDefinitionField.choice_values_it-it'
        db.delete_column('form_designer_formdefinitionfield', 'choice_values_it-it')

        # Deleting field 'FormDefinitionField.choice_values_es-es'
        db.delete_column('form_designer_formdefinitionfield', 'choice_values_es-es')

        # Deleting field 'FormDefinitionField.choice_labels_it-it'
        db.delete_column('form_designer_formdefinitionfield', 'choice_labels_it-it')

        # Deleting field 'FormDefinitionField.choice_labels_es-es'
        db.delete_column('form_designer_formdefinitionfield', 'choice_labels_es-es')

        # Deleting field 'FormDefinition.title_it-it'
        db.delete_column('form_designer_formdefinition', 'title_it-it')

        # Deleting field 'FormDefinition.title_es-es'
        db.delete_column('form_designer_formdefinition', 'title_es-es')

        # Deleting field 'FormDefinition.mail_to_it-it'
        db.delete_column('form_designer_formdefinition', 'mail_to_it-it')

        # Deleting field 'FormDefinition.mail_to_es-es'
        db.delete_column('form_designer_formdefinition', 'mail_to_es-es')

        # Deleting field 'FormDefinition.mail_subject_it-it'
        db.delete_column('form_designer_formdefinition', 'mail_subject_it-it')

        # Deleting field 'FormDefinition.mail_subject_es-es'
        db.delete_column('form_designer_formdefinition', 'mail_subject_es-es')

        # Deleting field 'FormDefinition.success_message_it-it'
        db.delete_column('form_designer_formdefinition', 'success_message_it-it')

        # Deleting field 'FormDefinition.success_message_es-es'
        db.delete_column('form_designer_formdefinition', 'success_message_es-es')

        # Deleting field 'FormDefinition.error_message_it-it'
        db.delete_column('form_designer_formdefinition', 'error_message_it-it')

        # Deleting field 'FormDefinition.error_message_es-es'
        db.delete_column('form_designer_formdefinition', 'error_message_es-es')

        # Deleting field 'FormDefinition.submit_label_it-it'
        db.delete_column('form_designer_formdefinition', 'submit_label_it-it')

        # Deleting field 'FormDefinition.submit_label_es-es'
        db.delete_column('form_designer_formdefinition', 'submit_label_es-es')

        # Deleting field 'FormDefinition.message_template_it-it'
        db.delete_column('form_designer_formdefinition', 'message_template_it-it')

        # Deleting field 'FormDefinition.message_template_es-es'
        db.delete_column('form_designer_formdefinition', 'message_template_es-es')


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
            'error_message_es-es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_it-it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'form_template_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_data': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'mail_from': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_en': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_es-es': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_fr-be': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_it-it': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_nl': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_nl-be': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_nl-nl': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_en': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_es-es': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_fr-be': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_it-it': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_nl': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_nl-be': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_nl-nl': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'message_template_en': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_es-es': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_fr-be': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_it-it': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_nl': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_nl-be': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_nl-nl': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'default': "'POST'", 'max_length': '10'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'submit_label_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_es-es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_it-it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_clear': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'success_message_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_es-es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_it-it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_redirect': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_es-es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_it-it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'form_designer.formdefinitionfield': {
            'Meta': {'object_name': 'FormDefinitionField'},
            'choice_labels_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_es-es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_fr-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_it-it': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_nl-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_nl-nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_model': ('form_designer.model_name_field.ModelNameField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'choice_model_empty_label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'choice_values_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_es-es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_fr-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_it-it': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_nl-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_nl-nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'decimal_places': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'field_class': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'form_definition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['form_designer.FormDefinition']"}),
            'help_text_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_es-es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_it-it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_result': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'initial_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_es-es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_it-it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_es-es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_it-it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
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
