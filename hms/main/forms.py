#encoding:utf-8
from django.forms import ModelForm, Form
from django import forms
from hms.main.models import Contact

class ContactForm(ModelForm):
    class Meta:
        	model = Contact

class ContactFormT(ModelForm):
    class Meta:
        	model = Contact
        	exclude = ('contact_type',)

class ContacttForm(Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class EmailForm(Form):
    subject = forms.CharField(label='Tema',required= True)
    email = forms.EmailField(required=False)
    message = forms.CharField(label='Mensaje', required= True, widget=forms.Textarea)

