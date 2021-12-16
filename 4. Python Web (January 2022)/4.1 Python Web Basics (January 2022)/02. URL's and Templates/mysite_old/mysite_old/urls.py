from django.contrib import admin
from django.urls import path, include

from mysite_old.cities.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path('cities/', include('mysite_old.cities.urls')),
    path('people/', include('mysite_old.people.urls')),
]
