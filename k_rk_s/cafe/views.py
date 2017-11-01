from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView

from cafe.models import Cafe


class ShowCafeView(ListView):
    model = Cafe
    template_name = 'landing.html'

    def get_queryset(self):
        return Cafe.objects.all()