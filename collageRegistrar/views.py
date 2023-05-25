from django.shortcuts import render,redirect
from .forms import *
from.models import *
from rest_framework.response import Response
from rest_framework.views import *
from .serializers import *
from datetime import datetime, timedelta

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

class AnnouncementApi(APIView):
    def get(self,req,*args,**kwargs):
        announcements= Announcement.objects.all().order_by('-id')
        actives =[]
        for annou in announcements:
            dateint= int(str(annou.announcement_time)[8:10])
            datemonthint= int(str(annou.announcement_time)[5:7])
            datetoday = datetime.now()
            dateNowINt= int(str(datetoday)[8:10])
            dateNowMINt= int(str(datetoday)[5:7])
            if (datemonthint-dateNowMINt)==0:
                if abs(dateNowINt- dateint)<=7: 
                    actives.append(annou)
        serializer = AnnouncementSerializer(actives, many= True)
        return Response(serializer.data)
def courseRegistration(req):
   
        context={
            'secondYrCS': "{"+ f"'data': '2023 registration form'"+"}",
        }
        return render(req,'collage/home.html',context)
    # else:
    #     return render(req,'collage/home.html')




class CourseReg(APIView):
    def post(self, request, format=None):
        serializer = CourseRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserData(APIView):
    def post(self, req, format= None):
        user = users.objects.filter(email= req.data)
        udata= UserSerializer(data= user)
        return Response(udata.data)

def getUser(req):
    print(req.post)
    return redirect('register_course')
    

