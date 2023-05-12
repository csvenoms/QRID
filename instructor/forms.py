from django import forms
from dashboard.models import courseMaterial
from instructor.models import attendance

class MaterialForm(forms.ModelForm):
    
    class Meta:
        model = courseMaterial
        fields = '__all__'
        
        
class qrAttendanceForm(forms.ModelForm):
    
    class Meta:
        model = attendance
        fields = "__all__"