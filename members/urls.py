from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
# from chat.views import room
urlpatterns = [
    # path('',views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/',views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
