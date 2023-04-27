from django.urls import path
from . import views
urlpatterns=[
    path('post', views.postAnnouncement),
    # path('get', views.getAnnouncement),
    path('getAnnouncementAPI', views.getAnnouncementAPI),
]