#encoding:utf-8
from django.forms import ModelForm
from django import forms
from hms.main.models import Contact

class ContactForm(ModelForm):
    class Meta:
        	model = Contact

class ContactFormT(ModelForm):
    class Meta:
        	model = Contact
        	exclude = ('contact_type',)

