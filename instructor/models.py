from django.db import models
from datetime import date
# Create your models here.
class attendance(models.Model):
    stud_id= models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    course_title= models.CharField( max_length=50)
    department=models.CharField( max_length=50)
    def __str__(self):
        return self.stud_id+"-"+ self.course_title+" on "+self.date
    