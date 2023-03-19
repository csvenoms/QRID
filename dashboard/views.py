from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from.forms import *
# Create your views here.

def dashboard(req):
    return render(req, "dashboard/index.html")


def reg(req):
    if req.method== "POST":
        form = RegisterStudentForm(req.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterStudentForm()
    context={
        'form':form
    }
    return render(req,'dashboard/register.html',context)