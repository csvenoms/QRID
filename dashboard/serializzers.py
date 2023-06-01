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

from django.contrib.auth.models import User
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile_picture')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)