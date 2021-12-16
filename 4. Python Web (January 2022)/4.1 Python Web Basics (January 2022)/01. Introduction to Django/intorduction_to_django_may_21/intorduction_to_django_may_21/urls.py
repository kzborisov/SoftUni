from django.contrib import admin
from django.urls import path
from intorduction_to_django_may_21.cities.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]
