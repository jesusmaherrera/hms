#encoding:utf-8
from django.forms import ModelForm
from django import forms
from hms.main.models import Contact

class ContactForm(ModelForm):
    class Meta:
          model = Contact



