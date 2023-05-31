from django.contrib import admin
from django.urls import path,include
from . import views 



urlpatterns = [
# path('', AjaxPost.MyAPIView.as_view(), name = 'sendMessage'), # FBV
path('', views.chat, name= "sendMessage"),
path('getMessage/<str:pk>', views.gmessages, name= "getMessage"),
path('getMessageAPI/<str:pk>', views.GetMessages.as_view()),
path('sendMessage>', views.postMessage, name= "sendMessage"),
 
# path('ajax/contact', AjaxPost.postMessage, name ='sendMessage'),
# path('', AjaxPost.ContactAjax.as_view(), name = 'sendMessage')
]