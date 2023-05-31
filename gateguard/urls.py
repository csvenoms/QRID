from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.checkID, name= "checkID"),
    #path("guardhome", views.regpc, name="registerpc"),
    path("registerPC/", views.regpc, name="registerpc"),
    path("checkPC/", views.checkpc, name="checkpc"),
]
