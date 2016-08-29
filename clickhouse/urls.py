from django.conf import settings
from django.conf.urls import url
from views import api, dashboard

urlpatterns = [
  url(r'api/$', api),
  url(r'dashboard/$', dashboard)
]
