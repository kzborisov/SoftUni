from django.shortcuts import render, redirect

from ExpensesTracker.core.profile_utils import get_profile
from ExpensesTracker.web.forms import CreateExpenseForm, EditExpenseForm, DeleteExpenseForm
from ExpensesTracker.web.models import Expense


def index(request):
    profile = get_profile()

    if not profile:
        return redirect('create profile')

    expenses = Expense.objects.all()
    context = {
        'expenses': expenses,
        'budget': profile.budget,
        'budget_left': profile.budget_left,
    }

    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateExpenseForm()
    context = {
        'form': form,
    }
    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditExpenseForm(instance=expense)
    context = {
        'expense': expense,
        'form': form,
    }
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('index')
    else:
        form = DeleteExpenseForm(instance=expense)
    context = {
        'expense': expense,
        'form': form,
    }
    return render(request, 'expense-delete.html', context)
