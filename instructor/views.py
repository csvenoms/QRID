from django.shortcuts import render
from django.contrib.auth.decorators import *
from dashboard.models import Course
from. forms import *
# Create your views here.
@login_required
def instructorHome(req):
    o=Course.objects.get(course_title="Introductio to Arteficial Intelegence")
    print(o.pk)
    # if req.method == 'POST':
        
    #     forms= courseMaterial(1,"asd", "asd",req.POST['file'])
       
    #     forms.save()
    # else:
    #     forms= MaterialForm()
    return render(req,'instructor/home.html')