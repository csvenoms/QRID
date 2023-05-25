from rest_framework import serializers
from .models import *
from dashboard.models import users
class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

class CourseRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRegitration
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'