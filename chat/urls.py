from django.contrib import admin
from django.urls import path
from . import views
from . import consumers

urlpatterns = [
    path('chat/<int:pk>/', views.room, name='home'),
    path('getroom/', views.getroom, name='getroom'),
    path('message/<int:pk>/', views.message, name='message'),
    path('message/<int:pk>/', views.message_sent, name='message_sent'),
    path('delete_message/<int:pk>/', views.delete_message, name='delete_message'),
    path('ws/messages/', consumers.MessageConsumer.as_asgi()),
]
