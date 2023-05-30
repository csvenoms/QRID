from django.forms import ModelForm
from . models import *
class AnnForm(ModelForm):
    class Meta:
        model = Announcement
        fields=['announcer','announcement']


class GradesForm(ModelForm):
    class Meta:
        model= GradeCSVs
        fields=  "__all__"
