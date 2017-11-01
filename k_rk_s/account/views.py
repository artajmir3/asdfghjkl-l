from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from account.forms.user_forms import SignUpForm


class SignUpView(FormView):
    success_url = '/admin/'
    form_class = SignUpForm
    template_name = 'signup.html'

    #def dispatch(self, request, *args, **kwargs):
    #    request.session.set_test_cookie()
    #    return super(SignUpView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = User()
        user.username = form.data['username']
        user.password = form.data['password']
        user.save()
        user = authenticate(username=user.username, password=user.password)
        login(self.request, user)
        return super(SignUpView, self).form_valid(form)


class HomeView(TemplateView):
    template_name = 'index.html'
