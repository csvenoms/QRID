from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.checkID, name= "checkID"),
    path("registerPC", views.regpc, name="registerpc"),
]
