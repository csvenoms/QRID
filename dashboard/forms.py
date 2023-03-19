from django import forms

from dashboard.models import users

class RegisterStudentForm(forms.ModelForm):
    
    class Meta:
        model = users
        fields = ['first_name','last_name','email','phone_no','student_id','student_department','batch','password','password']
