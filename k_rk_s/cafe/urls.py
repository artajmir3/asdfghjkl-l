from django.conf.urls import url

from cafe.views import ShowCafeView

urlpatterns = [
    url(r'^home'r'/$', ShowCafeView.as_view(), name='showcafe'),
    # url(r'^home/?q<search_id>'r'/$', ShowSearchView.as_view(), name='showsearchcafe'),
    # url(r'^cafe-autocomplete/$', CafeAutoCompleteView.as_view(), name= 'cafe-autocomplete')
]
