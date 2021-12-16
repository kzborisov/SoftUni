# Cities.urls
from django.urls import path

from mysite_old.cities.views import index

urlpatterns = [
    path('', index),
]
