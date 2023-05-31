from rest_framework.decorators import api_view
import csv
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import io
import json
from datetime import datetime, timedelta
from .serializers import *
from rest_framework.views import *
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from dashboard.models import users
from django.http import JsonResponse
<<<<<<< HEAD
=======
from dashboard.forms import CourseForm



>>>>>>> 89b72ec054789653b81752bb19cd4efad35c8598

def caesar_encrypt(plaintext, shift):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            ascii_code = ord(char)
            shifted_ascii_code = ascii_code + shift
            if char.isupper():
                if shifted_ascii_code > ord('Z'):
                    shifted_ascii_code -= 26
                elif shifted_ascii_code < ord('A'):
                    shifted_ascii_code += 26
            else:
                if shifted_ascii_code > ord('z'):
                    shifted_ascii_code -= 26
                elif shifted_ascii_code < ord('a'):
                    shifted_ascii_code += 26
            ciphertext += chr(shifted_ascii_code)
        else:
            ciphertext += char
    return ciphertext  # Create your views here.


def postAnnouncement(req):
    if req.method == "POST":
        form = AnnForm(req.POST, req.FILES)
        if form.is_valid:
            form.save()
    else:
        form = AnnForm()
    context = {
        'form': form
    }
    return render(req, 'collage/post.html', context)


class AnnouncementApi(APIView):
    def get(self, req, *args, **kwargs):
        announcements = Announcement.objects.all().order_by('-id')
        actives = []
        for annou in announcements:
            dateint = int(str(annou.announcement_time)[8:10])
            datemonthint = int(str(annou.announcement_time)[5:7])
            datetoday = datetime.now()
            dateNowINt = int(str(datetoday)[8:10])
            dateNowMINt = int(str(datetoday)[5:7])
            if (datemonthint-dateNowMINt) == 0:
                if abs(dateNowINt - dateint) <= 7:
                    actives.append(annou)
        serializer = AnnouncementSerializer(actives, many=True)
        return Response(serializer.data)


def courseRegistration(req):
    plainText = "{" + f"'data': '{datetime.now().year} registration form'"+"}"
    shift = 3
    encrypted_text = caesar_encrypt(plainText, shift)
    if req.method == 'POST':
        csv_file = req.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        for row in reader:
            CourseRegitration.objects.create(
                email=row['email'],
                fullName=row['fullName'],
                sex=row['sex'],
                year=row['year'],
                date_of_birth=row['date_of_birth'],
                mothers_fullName=row['mothers_fullName'],
                address_region=row['address_region'],
                address_zone=row['address_zone'],
                address_woreda=row['address_woreda'],
                address_kebele=row['address_kebele'],
                adress_city=row['adress_city'],
                address_houseNo=row['address_houseNo'],
                address_POBox=row['address_POBox'],
                prep_school_name=row['prep_school_name'],
                prep_complete_date=row['prep_complete_date'],
                prep_school_region=row['prep_school_region'],
                prep_school_zone=row['prep_school_zone'],
                prep_school_woreda=row['prep_school_woreda'],
                prep_school_kebele=row['prep_school_kebele'],
                prep_school_city=row['prep_school_city'],
                collage_join_year=row['collage_join_year'],
                department=row['department'],
                date_of_withdrawal=row['date_of_withdrawal'],
                demanded_service=row['demanded_service'],
                demand_Service_cashkind=row['demand_Service_cashkind'],
                estimated_cost=row['estimated_cost'],
                date_of_advance_payment=row['date_of_advance_payment'],
                semister=row['semister'],


            )
    context = {
        'secondYrCS': encrypted_text,
        'form': GradesForm(),
<<<<<<< HEAD
=======
        # 'course_form': CourseForm()
>>>>>>> 89b72ec054789653b81752bb19cd4efad35c8598
    }
    return render(req, 'collage/home.html', context)
    # else:
    #     return render(req,'collage/home.html')


userSet = {0, }


class CourseReg(APIView):
    def post(self, request, format=None):
        if request.data['email'] in userSet:
            return (Response({"message": "user already regestered"}))
        else:
            userSet.add(request.data['email'])
            serializer = CourseRegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserData(APIView):
    def post(self, req, format=None):
        user = users.objects.filter(email=req.data)
        udata = UserSerializer(data=user)
        return Response(udata.data)


def getUser(req):
    print(req.post)
    return redirect('register_course')


updateSet = {0, }


class MyModelUpdateAPIView(APIView):
    def get_object(self, pk):
        try:
            return CourseRegitration.objects.get(email=pk)
        except CourseRegitration.DoesNotExist:
            return None

    def put(self, request, pk, format=None):
        print(pk)
        print(updateSet)
        if pk in updateSet:
            return Response({"message": "already registered!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            mymodel = CourseRegitration.objects.get(email=pk)

            if mymodel is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            updateSet.add(pk)
            print(updateSet)
            data1 = json.loads(request.data)

            serializer = CourseRegistrationSerializer(
                mymodel, data=data1, partial=True)
            if serializer.is_valid():

                serializer.save()
                return Response(serializer.data)
            else:
                print("serializer not valied")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def submitGrades(req):
    return HttpResponse("<h1>insert each users grade from a csv file to the grades table</h1>")


def updateUserProfile(req):
    return HttpResponse("<h1>update user batch, or delete grad user from the main user table</h1>")

<<<<<<< HEAD
=======

def assignInstructor(req):
    return HttpResponse("<h1>assign instructor course, dept and batch</h1>")


def generate_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mymodel.csv"'

    writer = csv.writer(response)
    writer.writerow(['email', 'fullName', 'sex', 'year', 'date_of_birth', 'mothers_fullName', 'address_zone', 'address_region', 'address_woreda', 'address_kebele', 'adress_city', 'address_houseNo', 'address_POBox', 'prep_school_name', 'prep_complete_date',
                    'prep_school_region', 'prep_school_zone', 'prep_school_woreda', 'prep_school_kebele', 'prep_school_city', 'collage_join_year', 'department', 'date_of_withdrawal', 'demanded_service', 'demand_Service_cashkind', 'estimated_cost', 'date_of_advance_payment', 'semister'])

    my_model_data = CourseRegitration.objects.all().values_list('email', 'fullName', 'sex', 'year', 'date_of_birth', 'mothers_fullName', 'mothers_fullName', 'address_region', 'mothers_fullName', 'address_woreda', 'address_kebele', 'adress_city', 'address_houseNo', 'address_POBox', 'prep_school_name',
                                                                'prep_complete_date', 'prep_school_region', 'prep_school_zone', 'prep_school_woreda', 'prep_school_kebele', 'prep_school_city', 'collage_join_year', 'department', 'date_of_withdrawal', 'demanded_service', 'demand_Service_cashkind', 'estimated_cost', 'date_of_advance_payment', 'semister')
    for row in my_model_data:
        writer.writerow(row)

    return response


def my_view(request):
    return redirect('courseRegistration')


def upload_csv(request):
    context = {

        'form': GradesForm()
    }
    if request.method == 'POST':

        form = GradesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courseRegistration')
    return render(request, 'upload_csv.html', context)


class GetGradeResult(APIView):
    def get(self, request,pk, *args, **kwargs):
        search_attr = pk
        result = search_csv(search_attr)
        data_dict = json.loads(result)
        json_string = json.dumps(data_dict)


        return Response(data_dict)


def search_csv(search_attr):
    u = users.objects.get(email=search_attr)
    GetCsv = GradeCSVs.objects.get(dept=u.student_department.department, batch=u.batch)
    csv_file = GetCsv.csv_file

    # Read the CSV file and search for the attribute
    csv_data = csv_file.read().decode('utf-8')
    reader = csv.DictReader(csv_data.splitlines())
    print('read')
    for row in reader:
        print(row['email'])
        if row['email'] == search_attr:

            print('found')
            return json.dumps(row)
    data = {'s': 'mdn'}
    return data

from dashboard.models import Course
# Example usage
def insertcoursesfromcsv(req):
    if req.method=="POST":
        csv_file = req.FILES['csv_file']
        csv_data = csv_file.read().decode('utf-8')
        reader = csv.DictReader(csv_data.splitlines())
        print('read')
        for row in reader:
            course= Course.objects.create(
            course_title= row['course_title'],
            course_code= row['course_code'],
            credit_hour= row['credit_hour'],
            semister= row['semister'],
            target_group= row['target_group'],
            year=row['year'],
            )

        return redirect('courseRegistration')

class SemisterCoursesAPI(APIView):
    def get(self, request,pk):
        my_object = users.objects.filter(email=pk).first()
        sem= CourseRegitration.objects.filter(email=pk)
        print(my_object.student_department.department)
        print(my_object.batch)
        courses= Course.objects.filter(target_group = my_object.student_department.department, year = my_object.batch, semister= "I")


        
        serializer = CourseSerializer(courses, many=True)

        # Return the serialized data
        return Response(serializer.data)            
>>>>>>> 89b72ec054789653b81752bb19cd4efad35c8598

def assignInstructor(req):
    return HttpResponse("<h1>assign instructor course, dept and batch</h1>")


def generate_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mymodel.csv"'

    writer = csv.writer(response)
    writer.writerow(['email', 'fullName', 'sex', 'year', 'date_of_birth', 'mothers_fullName', 'address_zone', 'address_region', 'address_woreda', 'address_kebele', 'adress_city', 'address_houseNo', 'address_POBox', 'prep_school_name', 'prep_complete_date',
                    'prep_school_region', 'prep_school_zone', 'prep_school_woreda', 'prep_school_kebele', 'prep_school_city', 'collage_join_year', 'department', 'date_of_withdrawal', 'demanded_service', 'demand_Service_cashkind', 'estimated_cost', 'date_of_advance_payment', 'semister'])

    my_model_data = CourseRegitration.objects.all().values_list('email', 'fullName', 'sex', 'year', 'date_of_birth', 'mothers_fullName', 'mothers_fullName', 'address_region', 'mothers_fullName', 'address_woreda', 'address_kebele', 'adress_city', 'address_houseNo', 'address_POBox', 'prep_school_name',
                                                                'prep_complete_date', 'prep_school_region', 'prep_school_zone', 'prep_school_woreda', 'prep_school_kebele', 'prep_school_city', 'collage_join_year', 'department', 'date_of_withdrawal', 'demanded_service', 'demand_Service_cashkind', 'estimated_cost', 'date_of_advance_payment', 'semister')
    for row in my_model_data:
        writer.writerow(row)

    return response


def my_view(request):
    return redirect('courseRegistration')


def upload_csv(request):
    context = {

        'form': GradesForm()
    }
    if request.method == 'POST':

        form = GradesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courseRegistration')
    return render(request, 'upload_csv.html', context)


class GetGradeResult(APIView):
    def get(self, request,pk, *args, **kwargs):
        search_attr = pk
        result = search_csv(search_attr)
        data_dict = json.loads(result)
        json_string = json.dumps(data_dict)


        return Response(data_dict)


def search_csv(search_attr):
    u = users.objects.get(email=search_attr)
    GetCsv = GradeCSVs.objects.get(dept=u.student_department.department, batch=u.batch)
    csv_file = GetCsv.csv_file

    # Read the CSV file and search for the attribute
    csv_data = csv_file.read().decode('utf-8')
    reader = csv.DictReader(csv_data.splitlines())
    print('read')
    for row in reader:
        print(row['email'])
        if row['email'] == search_attr:

            print('found')
            return json.dumps(row)
    data = {'s': 'mdn'}
    return data


# Example usage
