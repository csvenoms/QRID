from django.db import models

# Create your models here.
class Announcement(models.Model):
    
    announcer= models.CharField(max_length=50)
    
    def uploadAnnouncement(self,filename):
        return f"announcement\{self.announcer}\{filename}"
    announcement= models.ImageField(upload_to=uploadAnnouncement)
    announcement_time= models.DateTimeField(auto_now_add= True)
    is_active = models.BooleanField(default=True)
    deactivated_at = models.DateTimeField(null=True, blank=True)

    def deactivate(self, duration_minutes=1):
        self.deactivated_at = announcement_time + timezone.timedelta(minutes=duration_minutes)
        self.save()

    def __str__(self):
        return self.announcer

class CourseRegitration(models.Model):
    fullName= models.CharField(max_length=100)
    sex= models.CharField( max_length=50)
    date_of_birth= models.DateField(auto_now=False, auto_now_add=False)
    mothers_fullName= models.CharField(max_length=100)
    address_region=models.CharField(max_length=100)
    address_zone=models.CharField(max_length=100)
    address_woreda=models.CharField(max_length=100)
    address_kebele=models.CharField(max_length=100)
    adress_city= models.CharField(max_length=100)
    address_houseNo=models.CharField(max_length=100)
    address_POBox=models.CharField(max_length=100)
    prep_school_name= models.CharField(max_length=100)
    prep_complete_date= models.DateField(auto_now= False, auto_now_add= False)
    prep_school_region=models.CharField(max_length=100)
    prep_school_zone=models.CharField(max_length=100)
    prep_school_woreda=models.CharField(max_length=100)
    prep_school_kebele=models.CharField(max_length=100)
    prep_school_city=models.CharField(max_length=100)
    collage_join_year= models.DateField(auto_now= False, auto_now_add=False)
    department= models.CharField(max_length=100)
    date_of_withdrawal= models.DateField(auto_now= False, auto_now_add=False, null=True)
    demanded_service= models.CharField(max_length=100)
    demand_type= models.CharField(max_length=100)
    estimated_cost=models.CharField(max_length=100)
    date_of_advance_payment=models.DateField(auto_now=False,auto_now_add= False, null=True)
    
    
    def __str__(self):
        return self.fullName


    
    