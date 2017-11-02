# from idlelib import autocomplete

# from dal import autocomplete
from django.http.request import QueryDict
from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView

from cafe.models import Cafe


class ShowCafeView(ListView):
    model = Cafe
    template_name = 'landing.html'

    def get_queryset(self):
        search_id = ''
        if len(self.request.GET)== 0:
            search_id = ''
        else:
            search_id = self.request.GET.get('s')
        # a = QueryDict()
        # a.get()
        print(search_id)
        return Cafe.objects.filter(name__contains=search_id)


# class CafeAutoCompleteView(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         cs = Cafe.objects.all()
#
#         if self.q:
#             cs = cs.filter(name__startswith=self.q)
#         return cs

# class ShowSearchView(ListView):
#     model = Cafe
#     template_name = 'all.html'
#
#     def get_context_data(self, **kwargs):
#         print(self.request.GET)
#         print(kwargs['search_id'])
#         return Cafe.objects.contains(kwargs['search_id'])