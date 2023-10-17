from typing import Any
from django import forms
from .models import Notes
from django.core.exceptions import ValidationError


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-5'})
        }
        labels = {
            'text': 'Escribe tus pensamientos:'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise forms.ValidationError("Title must contain Django")
        return title

    def clean_text(self):
        text = self.cleaned_data['text']

        if len(text) < 20:
            raise forms.ValidationError("Text must be greater than 20 characters")

        return text