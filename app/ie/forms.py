from django.core.exceptions import ImproperlyConfigured
from django.db.models import fields
from django import forms
class Image_form(forms.Form):
    image = forms.ImageField()