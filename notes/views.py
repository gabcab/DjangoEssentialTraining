from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"


# def list(request):
#     all_notes = Notes.objects.all()
#     print(all_notes)
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Nota no existe.")
#     return render(request, 'notes/notes_detail.html', {'note': note})

