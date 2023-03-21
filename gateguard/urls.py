from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.home, name='guardhome'),
    path('contact/', views.contact, name='contact'),
    path('searched/', views.searchbar, name='searched'),
    path('update1/', views.update1, name='update1'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
