from rest_framework import serializers
from .models import *

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = attendance
        fields = ['stud_id','course_title','department', 'date']