from django.conf import settings
from django.conf.urls import url
from views import api

urlpatterns = [
  url(r'api/$', api)
]
