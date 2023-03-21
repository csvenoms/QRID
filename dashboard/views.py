from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from.forms import *
from django.contrib import messages,auth
# Create your views here.

def dashboard(req):
    return render(req, "dashboard/index.html")


def reg(req):
    if req.method== "POST":
       
            form = RegisterStudentForm(req.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
    else:
        form = RegisterStudentForm()
    context={
        'form':form
    }
    return render(req,'dashboard/register.html',context)


def login(request):
    print("in the method")
    if request.method=='POST':
        print("in the post")

        email = request.POST['email']
        p = request.POST['password']
        user= auth.authenticate(email= email, password = p)
        print("is authd")

        if user is not None:
            print("user found")
          
            u=user.roll
            auth.login(request,user)
            if str(u) == 'Student':
                return redirect('instructorHome')
            elif str(u) == 'Instructor':
                return redirect('instructorHome')
            elif str(u) == 'user':
                return redirect('home')
        else:
            messages.error(request, 'wrong username or password')
    context={
        "form": LoginiForm()
    }
    return render(request,'dashboard/login.html',context)


def logout(request):
    auth.logout(request)
    return redirect('login')