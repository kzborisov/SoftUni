from django.contrib import admin

from ExpensesTracker.web.models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass
