from django.forms import ModelForm
from .models import *
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model= RegisteredPcs
        # fields="__all__"
        fields=['first_name','last_name','ID_no','serial','model_name']

class PcUpdateForm(forms.ModelForm):
    class  Meta:
        model=RegisteredPcs
        fields=['serial','model_name']