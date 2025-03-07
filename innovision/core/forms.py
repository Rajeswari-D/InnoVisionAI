from django import forms
from .models import StartupIdea

class StartupIdeaForm(forms.ModelForm):
    class Meta:
        model = StartupIdea
        fields = ['title', 'description']
