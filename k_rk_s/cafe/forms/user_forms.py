# from dal import autocomplete

from django import forms

from cafe.models import Cafe


# class CafeSearch(forms.Modelforms):
#     cafename = forms.ModelChoiceField(queryset=Cafe.objects.all , widget=autocomplete.ModelSelect2(url='cafe-autocomplete'))
#