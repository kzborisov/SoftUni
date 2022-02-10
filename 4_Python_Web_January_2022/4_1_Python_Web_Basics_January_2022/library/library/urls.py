from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.library_app.urls')),
    path('profile/', include('library.profiles.urls')),
]
