from django.core.mail import send_mail, get_connection

from django.forms.widgets import TextInput

from django import forms

class ContactForm(forms.Form):
   name = forms.CharField(label='sr-only', widget=forms.TextInput(
   attrs={'placeholder': 'İsim', 'class': 'form-control', 'id':'c_name'}))

   email = forms.EmailField(label='sr-only', widget=forms.TextInput(
   attrs={'placeholder': 'E-mail', 'class': 'form-control', 'id':'c_email'}),
   required=False)

   message = forms.CharField(label='sr-only', widget=forms.TextInput(
   attrs={'placeholder': 'Mesaj', 'class': 'form-control', 'id':'c_message'}))