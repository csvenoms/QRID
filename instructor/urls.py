from django.urls import path
from . import views
urlpatterns = [
    path('instructorHome', views.instructorHome, name='instructorHome'),
    path('addMaterial', views.addMaterial, name='addMaterial'),
    path('attended', views.CreateAttendance.as_view(), name='getAttendance')
]
