from django.urls import path
from . import views
urlpatterns=[
    path('post', views.postAnnouncement),
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

]