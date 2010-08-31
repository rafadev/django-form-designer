from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from form_designer.forms import CMSFormDefinitionForm
from form_designer.models import CMSFormDefinition
from form_designer.views import process_form
from form_designer import settings

class FormDesignerPlugin(CMSPluginBase):
    model = CMSFormDefinition
    name = _("Form")
    admin_preview = False
    form = CMSFormDefinitionForm

    def render(self, context, instance, placeholder):
        if instance.form_definition.form_template_name:
            self.render_template = instance.form_definition.form_template_name
        else:
            self.render_template = settings.DEFAULT_FORM_TEMPLATE
        return process_form(context['request'], instance.form_definition, context, is_cms_plugin=True)
        

    def get_form(self, request, obj=None, **kwargs):
        Form = super(FormDesignerPlugin, self).get_form(request, obj, **kwargs)

        class FakeForm(object):
            def __init__(self, Form, site):
                self.Form = Form
                self.site = site
                self.base_fields = Form.base_fields

            def __call__(self, *args, **kwargs):
                form = self.Form(*args, **kwargs)
                form.for_site(self.site)
                return form
        return FakeForm(Form, self.cms_plugin_instance.page.site or self.page.site)


plugin_pool.register_plugin(FormDesignerPlugin)
