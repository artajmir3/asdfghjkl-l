from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm


class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
