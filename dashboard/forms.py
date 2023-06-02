from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *

class RegisterStudentForm(UserCreationForm):
    
    class Meta:
        model = users
        fields = ['first_name','last_name','email','phone_no','student_id','student_department','batch']
class LoginiForm(forms.ModelForm):
    
    class Meta:
        model = users
        fields = ['email','password']

class CourseForm(forms.ModelForm):
    class Meta:
        models= Course
        fields= "__all__"