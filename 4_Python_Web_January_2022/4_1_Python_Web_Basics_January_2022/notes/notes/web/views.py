from django.shortcuts import render, redirect

from notes.core.profile_utils import get_profile
from notes.web.forms import ProfileForm, AddNoteForm, EditNoteForm, DeleteNoteForm
from notes.web.models import Note


def index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    notes = Note.objects.all()
    context = {
        'notes': notes,
    }
    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddNoteForm()

    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditNoteForm(instance=note)

    context = {
        'form': form,
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('index')
    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'note': note,
        'form': form,
    }
    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note,
    }
    return render(request, 'note-details.html', context)


def show_profile(request):
    profile = get_profile()
    context = {
        'notes_count': Note.objects.all().count(),
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if profile:
        profile.delete()
        Note.objects.all().delete()
        return redirect('index')
