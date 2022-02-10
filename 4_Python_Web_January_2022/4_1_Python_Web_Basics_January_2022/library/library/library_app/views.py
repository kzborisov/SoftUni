from django.shortcuts import render, redirect

from library.core.profile_utils import get_profile
from library.library_app.forms import CreateBookForm, EditBookForm
from library.library_app.models import Book


def index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    context = {
        'profile': profile,
        'books': Book.objects.all(),
    }
    return render(request, "home-with-profile.html", context)


def add_book(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateBookForm()

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    profile = get_profile()
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditBookForm(instance=book)

    context = {
        'profile': profile,
        'book': book,
        'form': form,
    }
    return render(request, 'edit-book.html', context)


def delete_book(request, pk):
    profile = get_profile()
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('index')


def details_book(request, pk):
    profile = get_profile()
    book = Book.objects.get(pk=pk)
    context = {
        'profile': profile,
        'book': book,
    }
    return render(request, 'book-details.html', context)
