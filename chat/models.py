from django.db import models

# Create your models here.

class ChatMessage(models.Model):
    email= models.CharField(max_length= 250, default= "")
    name= models.CharField(max_length= 100, default= "")
    dept= models.CharField(max_length= 100, default="")
    batch= models.CharField(max_length= 100, default="")
    message= models.CharField(max_length= 100, default="",null=True)
    chfile = models.FileField(upload_to="img/", max_length=100, blank= True, null=True)
    time= models.DateTimeField(auto_now_add=True, auto_now=False)

