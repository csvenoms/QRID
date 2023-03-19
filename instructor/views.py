from django.shortcuts import render

# Create your views here.
def instructorHome(req):
    return render(req,'instructor/home.html')