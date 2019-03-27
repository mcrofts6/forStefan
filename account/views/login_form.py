from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime
from account import models as amod
from django.contrib.auth import authenticate
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError



class LoginForm(forms.Form):
    username = forms.CharField(label="Enter Username", max_length=50)
    password = forms.CharField(label="Enter Password", widget=forms.PasswordInput(), min_length=8)

    def clean(self):
        if authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password']) is None:
            raise ValidationError(_('Wrong username or password'))
        return self.cleaned_data