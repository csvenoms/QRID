from django.forms import ModelForm
from . models import *
from django import forms
class AnnForm(ModelForm):
    class Meta:
        model = Announcement
        fields="__all__"
        


class GradesForm(ModelForm):
    class Meta:
        model= GradeCSVs
        fields=  "__all__"
