from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(users)
admin.site.register(Collage)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(roll)
admin.site.register(courseMaterial)
admin.site.register(savedAnnouncements)
