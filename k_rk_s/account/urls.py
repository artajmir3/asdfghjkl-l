from django.conf.urls import url

from account.views import SignUpView, HomeView

urlpatterns = [
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
]
