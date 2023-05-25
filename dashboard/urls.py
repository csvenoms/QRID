from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard),
    path('reg',views.reg, name="home"),
    path('login',views.login, name="login"),
    path('getUserAnnouncements',views.GetSavedAnnouncements.as_view(), name="getUserAnnouncements"),
    path('getUserData/<str:pk>/', views.GetUserInfo.as_view(), name="getUserData"),

]
