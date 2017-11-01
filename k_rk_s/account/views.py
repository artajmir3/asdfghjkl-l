from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.forms.utils import ErrorList
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from account.forms.user_forms import SignUpForm


class SignUpView(FormView):
    success_url = '/home/'
    form_class = SignUpForm
    template_name = 'login.html'

    #def dispatch(self, request, *args, **kwargs):
    #    request.session.set_test_cookie()
    #    return super(SignUpView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        users = User.objects.all()
        for my_user in users:
            if my_user.username == form.data['username']:
                form.ra('user already exists')
                #return super(SignUpView, self).form_invalid(form)
        user = User()
        user.username = form.data['username']
        user.password = form.data['password']
        user.email = form.data['email']
        user.save()
        user = authenticate(username=user.username, password=user.password)
        login(self.request, user)
        return super(SignUpView, self).form_valid(form)



class HomeView(TemplateView):
    template_name = 'index.html'
