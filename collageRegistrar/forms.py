from django.forms import ModelForm
from .models import *
class AnnForm(ModelForm):
    class Meta:
        model = Announcement
        fields=['announcer','announcement']