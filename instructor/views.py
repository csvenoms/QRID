from datetime import date, time
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import *
from dashboard.models import Course
from instructor.models import *
from. forms import *
from django.contrib import messages
from datetime import date
from chat.forms import MessageForm


def caesar_encrypt(plaintext, shift):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            ascii_code = ord(char)
            shifted_ascii_code = ascii_code + shift
            if char.isupper():
                if shifted_ascii_code > ord('Z'):
                    shifted_ascii_code -= 26
                elif shifted_ascii_code < ord('A'):
                    shifted_ascii_code += 26
            else:
                if shifted_ascii_code > ord('z'):
                    shifted_ascii_code -= 26
                elif shifted_ascii_code < ord('a'):
                    shifted_ascii_code += 26
            ciphertext += chr(shifted_ascii_code)
        else:
            ciphertext += char
    return ciphertext
# Create your views here.
@login_required
def instructorHome(req):
    
    if req.method == 'POST':
              
        
        form = MaterialForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            messages.success(req,"Status= send")

        else:
            messages.error(req,"unable to send material")
                
         
    data ="{"+f"'course_title':'{req.user.instructor_course}','date':'{date.today()}','department':'{req.user.student_department}', 'targetGroup':'{req.user.instructor_course.target_group}', 'year': '{req.user.instructor_course.year}'"+","
    shift = 3
    encrypted_text = caesar_encrypt(data, shift)
    
    context={
        'form': MessageForm(),
        'course': encrypted_text,
    }
    
    return render(req,'instructor/home.html',context )

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializer import AttendanceSerializer

userSet={0,}
class CreateAttendance(CreateAPIView):
    
    serializer_class = AttendanceSerializer

    def post(self, request, *args, **kwargs):
        if request.data['stud_id'] in userSet:
            return(Response({"message":"user already attended"}))
        else:
            userSet.add(request.data['stud_id'])
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data)
    

            

@login_required
def addMaterial(req):
    if req.method == 'POST':           
        print('in addM') 
        form = MessageForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            messages.success(req,"sent successfully")

            return redirect('instructorHome')
        else:
            messages.error(req,"unable to send material")

            return redirect('instructorHome')