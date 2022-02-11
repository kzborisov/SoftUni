from django.urls import path

from recipes.recipes_app.views import index, edit_recipe, delete_recipe, details_recipe, create_recipe

urlpatterns = (
    path('', index, name='index'),
    path('create/', create_recipe, name='create recipe'),
    path('edit/<int:pk>/', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>/', delete_recipe, name='delete recipe'),
    path('details/<int:pk>/', details_recipe, name='details recipe'),
)
