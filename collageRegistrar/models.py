from django.db import models

# Create your models here.
class Announcement(models.Model):
    
    announcer= models.CharField(max_length=50)
    
    def uploadAnnouncement(self,filename):
        return f"announcement/{self.announcer}"
    announcement= models.ImageField(upload_to=uploadAnnouncement)
    announcement_time= models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.announcer+" "+str(self.announcement_time)
    