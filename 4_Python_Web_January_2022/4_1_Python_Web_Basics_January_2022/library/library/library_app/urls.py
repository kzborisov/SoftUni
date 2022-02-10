from django.urls import path

from library.library_app.views import index, add_book, edit_book, details_book, delete_book

urlpatterns = (
    path('', index, name='index'),
    path('add/', add_book, name='add book'),
    path('delete/<int:pk>/', delete_book, name='delete book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('details/<int:pk>/', details_book, name='details book'),
)
