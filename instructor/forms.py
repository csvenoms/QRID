from django import forms
from dashboard.models import courseMaterial

class MaterialForm(forms.ModelForm):
    
    class Meta:
        model = courseMaterial
        fields = '__all__'
