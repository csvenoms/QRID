from django.db import models

# Create your models here.
class RegisteredPcs(models.Model):
    ID_no= models.CharField(max_length=50, primary_key=True, unique=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    model_name=models.CharField(max_length=50)
    serial=models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.id_no