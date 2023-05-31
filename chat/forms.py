from .models import *
from django import forms


class MessageForm(forms.ModelForm):
    
    class Meta:
        model = ChatMessage
        fields = "__all__"


