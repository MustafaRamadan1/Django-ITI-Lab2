

from django import forms
from .models import Todo
from django.forms import TextInput

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
            'class': 'form-control'
            })
        }
