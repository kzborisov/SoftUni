# people.urls
from django.urls import path

from mysite_old.people.views import people, list_phones

urlpatterns = [
    path('', people),
    path('phones/', list_phones),
]
