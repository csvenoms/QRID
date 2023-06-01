from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


# Create your models here.
class Collage(models.Model):
    collage=  models.CharField(max_length=50, unique=True,primary_key=True)
    def __str__(self):
        return self.collage

class Department(models.Model):
    collage= models.ForeignKey(Collage,on_delete=models.CASCADE)
    department= models.CharField(max_length=50, unique=True,primary_key=True)

    def __str__(self):
        return self.department

class Course(models.Model):
    course_code= models.CharField(max_length=50,unique=True)
    course_title= models.CharField(max_length=50, unique=True,primary_key=True) 
    credit_hour = models.CharField(max_length=10)
    target_group=   models.CharField(max_length=50, default="")
    year = models.CharField(max_length=10, default="2nd")
    semister= models.CharField(max_length=12, default="I")
    def get(self,course_title):
        course_title=self.course_title
        return course_title

    def __str__(self):
        return self.course_title  
class roll(models.Model):
    roll= models.CharField(max_length=80, primary_key=True)
    def __str__(self):
        return self.roll
class userManager(BaseUserManager):
    def create_user(self,email,first_name,last_name, password=None):
        if not email:
            raise ValueError('Users must have an email adress.')
        if not first_name or not last_name:
            raise ValueError('Users must have an FullName adress.')
        if not password:
            raise ValueError('Users must have an password adress.')
        user = self.model(
            email= self.normalize_email(email),
            first_name = first_name,
            last_name= last_name,
            
        )
        user.set_password(password)
        user.save(using= self.db)
        return user
    def create_superuser(self,email,first_name,last_name, password):
        user = self.create_user(
            email= self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin= True
        user.is_staff= True
        user.is_superuser= True
        user.save(using= self.db)
        return user

class users(AbstractBaseUser):

    first_name= models.CharField(max_length=50, null=False)
    last_name= models.CharField(max_length=50, null=False)
    email= models.EmailField(unique=True, max_length=254, primary_key=True)
    phone_no= models.CharField(max_length=50, null=False)
    student_id=models.CharField(max_length=50,default='-')
    instructor_course= models.ForeignKey(Course,to_field='course_title', default='Introductio to Arteficial Intelegence', on_delete=models.CASCADE)
    student_department= models.ForeignKey(Department,to_field="department",default='.', on_delete=models.CASCADE)
    batch= models.CharField(max_length=50, null=False, default='-')
    image = models.ImageField(upload_to='images/', null= True)
    roll= models.ForeignKey(roll, on_delete=models.CASCADE,to_field="roll", default=".")
    date_joined= models.DateTimeField(auto_now_add= True)
    last_login= models.DateTimeField(auto_now=True)
    is_admin= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    objects= userManager()


    def __str__(self):
        return self.email
    def has_perm(self, perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
    def has_change_permission(self,request, obj=None):
        return True
    def has_delete_permission(self,request, obj=None):
        return True

def upload_filepath(self,filename):
    return f'Material/{self}/'

class courseMaterial(models.Model):
    
    course = models.CharField(max_length=255)
    chapter = models.CharField(max_length=255)
    title= models.CharField(max_length=255)
    
        
    def p(self,filename):
        return f'Material\{self.course}\{filename}'
    material= models.FileField( upload_to=p, max_length=255)
    
    def __str__(self) -> str:
        print(self.course)

        return  self.chapter +" "+ self.title
    


class savedAnnouncements(models.Model):
    user = models.CharField(max_length=50)
    announcer = models.CharField(max_length=50)
    announcement = models.CharField(max_length=50)

    
    def __str__(self):
        return self.user
    