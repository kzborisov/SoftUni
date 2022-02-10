from django.urls import path

from ExpensesTracker.profiles.views import show_profile, edit_profile, delete_profile, create_profile

urlpatterns = (
    path('', show_profile, name='show profile'),
    path('create/', create_profile, name='create profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),
)
