from django.urls import path
from . import views
urlpatterns=[
    path('post', views.postAnnouncement),
    # path('get', views.getAnnouncement),
    path('getAnnouncementAPI', views.AnnouncementApi.as_view(), name='getAnnouncemnets'),
]