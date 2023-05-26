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


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate a new RSA key pair
key = RSA.generate(2048)

# Create an instance of the RSA cipher with the public key
cipher = PKCS1_OAEP.new(key.publickey())

# Define the plaintext data to encrypt
   
def courseRegistration(req):
   
        context={
            'secondYrCS': "{"+ f"'data': '{datetime.now().year} registration form'"+"}",
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
from rest_framework.decorators import api_view
import io
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes

class MyModelUpdateAPIView(APIView):
    def get_object(self, pk):
        try:
            return CourseRegitration.objects.get(email=pk)
        except CourseRegitration.DoesNotExist:
            return None

    def put(self, request, pk, format=None):
        mymodel = CourseRegitration.objects.get(email=pk)

        if mymodel is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data1 = json.loads(request.data)
        # print(request.data['data'])
        # # mymodel.year= data['year']
        serializer = CourseRegistrationSerializer(mymodel, data=data1,partial=True)
        if serializer.is_valid():
            # print(serializer.data)

            serializer.save()
            return Response(serializer.data)
        else:
            print("serializer not valied")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        mymodel = self.get_object(pk)

        if mymodel is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CourseRegistrationSerializer(mymodel, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

