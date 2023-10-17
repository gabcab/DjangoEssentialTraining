from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render
from .models import Notes
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotesForm

# Create your views here.
class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    paginate_by = 2
    login_url="/admin"

    def get_queryset(self):
        return self.request.user.notes.all()


# def list(request):
#     all_notes = Notes.objects.all()
#     print(all_notes)
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Nota no existe.")
#     return render(request, 'notes/notes_detail.html', {'note': note})

class NotesCreateView(CreateView):
    model=Notes
    form_class=NotesForm 
    success_url = '/smart/notes'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())




class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model=Notes
    #fields=['title', 'text']
    form_class=NotesForm
    success_url = '/smart/notes/'

class NotesDelete(DeleteView):
    model=Notes
    success_url='/smart/notes'
