from django.shortcuts import render

# Create your views here.
def checkID(req):
    return render(req, 'gateguard/checkid.html')

def regpc(req):
    return render(req, 'gateguard/registerpc.html')