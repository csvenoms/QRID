from django.db import models

# Create your models here.
class RegisteredPcs(models.Model):
    id_no= models.CharField(max_length=50, primary_key=True, unique=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    serial_number=models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.id_no