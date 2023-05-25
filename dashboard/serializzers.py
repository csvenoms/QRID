from .models import *
from rest_framework import serializers
class UserAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = savedAnnouncements
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'