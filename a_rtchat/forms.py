from django.forms import ModelForm
from django import forms
from .models import *

class ChatMessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'class': 'p-4 text-black', 'placeholder': 'Type your message here...', 'max_length': 300, 'autofocus': True})
        }
        