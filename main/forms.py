from django import forms
from django.forms import ModelForm
from main.models import EmailListSignup
from django.http import HttpResponse
from django.shortcuts import render
import re

emailregex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

class EmailListSignupForm(ModelForm):
    class Meta:
        model = EmailListSignup
        fields = ['email']
    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        if re.match(emailregex, email):
            try:
                match = EmailListSignup.objects.get(email=email)
            except EmailListSignup.DoesNotExist:
                # Unable to find a user, this is fine
                return email

            # A user was found with this as a username, raise an error.
            raise forms.ValidationError('This email address is already in use.')
        else:
            raise forms.ValidationError('This is not a valid email address')
