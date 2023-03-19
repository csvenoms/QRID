from django.shortcuts import render

from dashboard.models import Course
from. forms import *
# Create your views here.
def instructorHome(req):
    o=Course.objects.get(course_title="Introductio to Arteficial Intelegence")
    print(o.pk)
    # if req.method == 'POST':
        
    #     forms= courseMaterial(1,"asd", "asd",req.POST['file'])
       
    #     forms.save()
    # else:
    #     forms= MaterialForm()
    return render(req,'instructor/home.html')