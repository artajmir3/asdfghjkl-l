from captcha.fields import CaptchaField
from django.contrib.admin import forms
from django.contrib.auth import forms, authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.fields import CharField
from django.forms.models import ModelForm
from django import forms
from django.forms.widgets import PasswordInput


class SignUpForm(ModelForm):
    passwordconfirmation = CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()


    def clean(self):
        super(SignUpForm, self).clean()
        if self.data['password'] != self.data['passwordconfirmation']:
            self.add_error('password' ,'password must match')
        users = User.objects.all()
        for my_user in users:
            if my_user.username == self.data['username']:
                self.add_error('username', 'user already exists')
        # if self.data['password'] == self.data['passwordconfirmation']:
        #     users = User.objects.all()
        #     for my_user in users:
        #         if my_user.username == self.data['username']:
        #             self.add_error('username' ,'user already exists')
        #             # return super(SignUpView, self).form_invalid(form)
        #     user = User()
        #     user.username = self.data['username']
        #     user.password = self.data['password']
        #     user.email = self.data['email']
        #     user.save()
        #     user = authenticate(username=user.username, password=user.password)
        #     login(self.request, user)
        #     return super(SignUpForm, self).clean()
        # else:
        #     self.add_error('password' ,'password must match')
        #     users = User.objects.all()
        #     for my_user in users:
        #         if my_user.username == self.data['username']:
        #             self.add_error('username', 'user already exists')
        #   #  raise ValidationError(('passwords must match'), code='invalid')

    def ra(self , st):
        raise ValidationError((st), code='invalid')

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        widgets = {
            'password': forms.PasswordInput(),
        }

    # def __init__(self, *args, **kwargs):
    #     super(SignUpForm, self).__init__(*args, **kwargs)
    #     self.fields['password'].widget = forms.PasswordInput
