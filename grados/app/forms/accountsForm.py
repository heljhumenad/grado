from django.contrib.auth.forms import AuthenticationForm
from django import forms

class CustomAuthenticationForm(AuthenticationForm):

    def clean(self):
        pass # TODO: Customize authentication message in the login forms