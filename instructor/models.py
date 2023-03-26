from django.db import models

# Create your models here.
class attendance(models.Model):
    stud_id= models.CharField(max_length=50,default='course_attendance')
    student_first_name =models.CharField(max_length=50, default="courseAttendance")
    date = models.DateField( auto_now=True, auto_now_add=True)
    time= models.TimeField( auto_now_add=True)
    course_title= models.CharField( max_length=50)
    
class qrAttendance(models.Model):
    qr= models.ImageField( upload_to='attendance/', height_field=None, width_field=None, max_length=None)
