from django.urls import path

from ExpensesTracker.web.views import index, create_expense, edit_expense, delete_expense

urlpatterns = (
    path('', index, name='index'),
    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>', edit_expense, name='edit expense'),
    path('delete/<int:pk>', delete_expense, name='delete expense'),
)
