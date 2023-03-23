from django import forms


class ContactForm(forms.Form):
    """ contact form for contact page"""
    full_name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=20)
    Registration = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50)
