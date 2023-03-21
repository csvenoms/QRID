from django import forms
from django.contrib.auth.forms import UserCreationForm

from dashboard.models import users

class RegisterStudentForm(UserCreationForm):
    
    class Meta:
        model = users
        fields = ['first_name','last_name','email','phone_no','student_id','student_department','batch',"password1","password2"]
class LoginiForm(forms.ModelForm):
    
    class Meta:
        model = users
        fields = ['email','password']

        