from django import forms
from dashboard.models import courseMaterial
from instructor.models import qrAttendance

class MaterialForm(forms.ModelForm):
    
    class Meta:
        model = courseMaterial
        fields = '__all__'
class qrAttendanceForm(forms.ModelForm):
    
    class Meta:
        model = qrAttendance
        fields = "__all__"
