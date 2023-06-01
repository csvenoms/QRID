from django.db import models

# Create your models here.
class Announcement(models.Model):
    
    announcer= models.CharField(max_length=50)
    
    def uploadAnnouncement(self,filename):
        return f"announcement\{self.announcer}\{filename}"
    announcement= models.ImageField(upload_to=uploadAnnouncement)
    announcement_time= models.DateTimeField(auto_now_add= True)
   
    

    def __str__(self):
        return self.announcer

class CourseRegitration(models.Model):
    email = models.CharField(max_length= 250, unique=True)
    fullName= models.CharField(max_length=100)
    sex= models.CharField( max_length=50)
    year= models.CharField(max_length=4, default="")
    date_of_birth= models.CharField(max_length=100, default= "")
    mothers_fullName= models.CharField(max_length=100)
    address_region=models.CharField(max_length=100)
    address_zone=models.CharField(max_length=100)
    address_woreda=models.CharField(max_length=100)
    address_kebele=models.CharField(max_length=100)
    adress_city= models.CharField(max_length=100)
    address_houseNo=models.CharField(max_length=100)
    address_POBox=models.CharField(max_length=100)
    prep_school_name= models.CharField(max_length=100)
    prep_complete_date= models.CharField(max_length=100, default= "")
    prep_school_region=models.CharField(max_length=100)
    prep_school_zone=models.CharField(max_length=100)
    prep_school_woreda=models.CharField(max_length=100)
    prep_school_kebele=models.CharField(max_length=100)
    prep_school_city=models.CharField(max_length=100)
    collage_join_year= models.CharField(max_length=100, default= "")
    department= models.CharField(max_length=100)
    date_of_withdrawal= models.CharField(null=True,max_length=100, default= "")
    demanded_service= models.CharField(max_length=100, default= "")
    demand_Service_cashkind= models.CharField(max_length=100, null=True)
    estimated_cost=models.CharField(null=True,max_length=100, default= "")
    date_of_advance_payment=models.CharField(max_length=100, default= "", null=True)
    semister= models.CharField(max_length= 3, default= "I")
    
    def __str__(self):
        return self.fullName


class GradeCSVs(models.Model):
    csv_file= models.FileField(upload_to="grades/")
    dept= models.CharField(max_length=100)
    batch= models.CharField(max_length=100)

    def __str__(self):
        return f"{self.batch}-{self.dept}"
        

    
