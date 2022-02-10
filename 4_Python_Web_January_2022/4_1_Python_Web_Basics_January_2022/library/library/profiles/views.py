from django.shortcuts import render, redirect

from library.core.profile_utils import get_profile
from library.library_app.models import Book
from library.profiles.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm


def show_profile(request):
    profile = get_profile()
    if profile:
        context = {
            'profile': profile,
        }
        return render(request, 'profile.html', context)
    return redirect('create_profile')


def create_profile(request):
    profile = get_profile()
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
            return redirect('show profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        Book.objects.all().delete()
        return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'delete-profile.html', context)
