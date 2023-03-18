from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def dashboard(req):
    return render(req, "dashboard/index.html")