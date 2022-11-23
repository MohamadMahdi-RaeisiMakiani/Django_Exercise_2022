from django.shortcuts import render
from django.http import Http404
from .models import MyNotes


def list_titles(request):
    all_Notes = MyNotes.objects.all()
    return render(request, 'texts_temp/title_of_notes.html', {'notes_obj': all_Notes})


def list_eachNote(request, pk):
    try:
        each_note = MyNotes.objects.get(pk=pk)
        return render(request, 'texts_temp/one__note.html', {'note_num': each_note})
    except MyNotes.DoesNotExist:
        raise Http404("There is no this number for notes!")


# python3 manage.py shell => to test ORM tables
# from notes.models import MyNotes
# Note_id1 = MyNotes.objects.get(pk='1')
# Note_id1.title
# Note_id1.text
# Note_id1.created
# Note_id1.objects.all()
# addNote = Note_id1.objects.create(title='Note Title', text='Note Text')
# MyNotes.objects.filter(title__startswith='Test').exclude(text__icontains='Book')
