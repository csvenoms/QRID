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
<<<<<<< HEAD
    
=======
>>>>>>> 89b72ec054789653b81752bb19cd4efad35c8598
