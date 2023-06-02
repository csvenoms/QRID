from django.urls import path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken
from .forms import *
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('post', views.postAnnouncement, name='postAnnouncement'),
    # path('get', views.getAnnouncement),
    path('getAnnouncementAPI', views.AnnouncementApi.as_view(), name='getAnnouncemnets'),
    path('courseRegistration', views.CourseReg.as_view(), name='courseRegistration'),
    path('registrarpage',views.courseRegistration, name= 'register_course'),
    path('getUserData',views.GetUserData.as_view(), name= 'getUser'),
    path('updateRegistrationData/<str:pk>', views.MyModelUpdateAPIView.as_view(), name="updateRegistration"),
    path('generate-csv/', views.generate_csv, name='generate_csv'),
    path('my-view/', views.my_view, name='my_view'),

    path('gradeInpput', views.upload_csv, name= "gradesubmission"),
    path('getGrade/<str:pk>/',views.GetGradeResult.as_view(), name= 'getGradeResult'),
    path('insertCourses', views.insertcoursesfromcsv, name= "insertCourses"),
    path('getSemisterCourses/<str:pk>/',views.SemisterCoursesAPI.as_view(), name= 'getSemisterCourses'),
    path('api-token-auth/', ObtainAuthToken.as_view()),
    path('change-password/', views.ChangePasswordView.as_view()),
    path('update', views.update, name="updateProf"),
    path('updateFromCSV', views.update_from_csv, name= "updateFromCSV"),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='collage/resetpassword.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt',
        form_class=MyPasswordResetForm
    ), name='password_reset'),
]