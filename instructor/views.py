from datetime import date, time
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import *
from dashboard.models import Course
from instructor.models import *
from. forms import *
from django.contrib import messages
from datetime import date
# Create your views here.
@login_required
def instructorHome(req):
    
    if req.method == 'POST':
              
        
        form = MaterialForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            
                
         
    data ="{"+f"'course_title':'{req.user.instructor_course}','date':'{date.today()}','department':'{req.user.student_department}', 'targerGroup':'{req.user.instructor_course.target_group}', 'year': '{req.user.instructor_course.year}'"+","
    context={
        'form':MaterialForm(),
        'course': data,
    }
    
    return render(req,'instructor/home.html',context )

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializer import AttendanceSerializer


class CreateAttendance(CreateAPIView):
    serializer_class = AttendanceSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)
    

            


def addMaterial(req):
    if req.method == 'POST':           
        print('in addM') 
        form = MaterialForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            print("aksdfhjhfa")
            return redirect('instructorHome')
        else:
            return redirect('instructorHome')