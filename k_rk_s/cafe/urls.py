from django.conf.urls import url

from cafe.views import ShowCafeView

urlpatterns = [
    url(r'^cafes/$', ShowCafeView.as_view(), name='showcafe'),
]
