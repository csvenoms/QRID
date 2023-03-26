from django.shortcuts import redirect, render
from django.contrib.auth.decorators import *
from dashboard.models import Course
from. forms import *
from django.contrib import messages

# Create your views here.
@login_required
def instructorHome(req):
    if req.method == 'POST':
              
        # print(type(req.POST['course']))
        # my_object = Course.objects.get(course_title= req.user.instructor_course)
        # my_object_as_string = str(my_object)
        # print(type(my_object_as_string))
        form = MaterialForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            print("aksdfhjhfa")
            
                
               
    
    context={
        'form':MaterialForm()
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