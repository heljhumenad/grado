from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext as _

class CustomAuthenticationForm(AuthenticationForm):
	error_messages = {
		"invalid_login": "Username and Password doesnt recognize by the system",
		"inactive": "Permission denied",
	}
	# BUG: when submitting the form non field error resetting the form
	def __init__(self, *args, **kwargs):	
		super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
		self.fields['username'].error_messages = {'required': "Username is required field"}
		self.fields['password'].error_messages = {'required': "Password is required field"}