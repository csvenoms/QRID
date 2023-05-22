from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from chat.views import room
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'authenticate/home.html')


def login_user(request):
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,'wrong login, letus try again')
            #return redirect('login')
            return render(request,'authenticate/login.html')
    
    else:
     return render(request,'authenticate/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,'You Are Loged Out')
    # return render(request,'authenticate/login.html')
    return redirect('login')

# def index(request):
#     return render(request, 'authenticate/index.html')
