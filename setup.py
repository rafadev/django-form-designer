from distutils.core import setup


setup(
    name='django-form-designer',
    version='0.1',
    description='A Django app for building many kinds of forms visually, without any programming knowledge.',
    author='Samuel Luescher',
    url='http://github.com/philomat',
    packages=[
        'form_designer',
        'form_designer.templatetags',
        'form_designer.migrations',
    ]
)
