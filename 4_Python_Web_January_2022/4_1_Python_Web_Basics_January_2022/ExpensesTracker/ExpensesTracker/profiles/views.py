from django.shortcuts import render, redirect

from ExpensesTracker.core.profile_utils import get_profile
from ExpensesTracker.profiles.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from ExpensesTracker.web.models import Expense


def show_profile(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        Expense.objects.all().delete()
        return redirect('index')

    form = DeleteProfileForm()
    context = {
        'form': form,
    }

    return render(request, 'profile-delete.html', context)
