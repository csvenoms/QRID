from datetime import date, time
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import *
from dashboard.models import Course
from instructor.models import qrAttendance
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
            
                
         
    data = f"{req.user.instructor_course},{date.today()}"
    context={
        'form':MaterialForm(),
        'course': data,
    }
    
    return render(req,'instructor/home.html',context )

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