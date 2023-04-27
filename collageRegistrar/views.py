from django.shortcuts import render
from .forms import *
from.models import *
from rest_framework.response import Response
# Create your views here.
def postAnnouncement(req):
    if req.method=="POST":
        form = AnnForm(req.POST,req.FILES)
        if form.is_valid:
            form.save()
    else:
        form= AnnForm()
    context = {
        'form':form
    }
    return render(req,'collage/post.html',context)

def getAnnouncementAPI(req):
    ann= Announcement.objects.all()
    data= {"announsor": ann.announcer,"announcement":ann.announcement.url,"announced": ann.announcement_time}
    return Response(data)