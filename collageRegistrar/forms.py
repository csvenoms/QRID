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
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from dashboard.models import users

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email", max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email'}))

    def get_users(self, email):
        return users.objects.filter(email__iexact=email, is_active=True)