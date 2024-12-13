from django.shortcuts import render, redirect, get_object_or_404
from .models import Note


def home(request):
    return render(request, 'index.html')


def note_list(request):
    notes = Note.objects.all()
    ctx = {'notes': notes}
    return render(request, 'notes/list.html', ctx)


def create_note(request):
    if request.method == "POST":
        note_title = request.POST.get('note_title')
        content = request.POST.get('content')
        if note_title and content:
            Note.objects.create(
                note_title=note_title,
                content=content,
            )
            return redirect('notes:list')
    return render(request, 'notes/form.html')


def update_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == "POST":
        note_title = request.POST.get('note_title')
        content = request.POST.get('content')
        if note_title and content:
            note.note=note_title,

            return redirect(note.get_detail_url())
    ctx = {'note': note}
    return render(request, 'notes/form.html', ctx)


def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    ctx = {'note': note}
    return render(request, 'notes/detail.html', ctx)


def note_delete(request, note_id):
        note = get_object_or_404(Note, pk=note_id)
        note.delete()
        return redirect('notes:list')