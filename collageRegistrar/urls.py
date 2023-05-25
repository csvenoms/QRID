from django.urls import path
from . import views
urlpatterns=[
    path('post', views.postAnnouncement),
    # path('get', views.getAnnouncement),
    path('getAnnouncementAPI', views.AnnouncementApi.as_view(), name='getAnnouncemnets'),
    path('courseRegistration', views.CourseReg.as_view(), name='courseRegistration'),
    path('registrarpage',views.courseRegistration, name= 'register_course'),
        path('getUserData',views.GetUserData.as_view(), name= 'getUser')


]