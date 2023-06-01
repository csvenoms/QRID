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

        def update(self, instance, validatedData):
            instance.email = validatedData.get('email', instance.email)
            instance.date_of_withdrawal = validatedData.get('date_of_withdrawal', instance.date_of_withdrawal)
            instance.demanded_service = validatedData.get('demanded_service', instance.demanded_service)
            instance.demand_Service_cashkind = validatedData.get('demand_Service_cashkind', instance.demand_Service_cashkind)
            instance.estimated_cost = validatedData.get('estimated_cost', instance.estimated_cost)
            instance.date_of_advance_payment = validatedData.get('date_of_advance_payment', instance.date_of_advance_payment)
            instance.semister = validatedData.get('semister', instance.semister)
            instance.year = validatedData.get('year', instance.year)
            instance.save()
            return instance
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'


        


class CourseRegistrationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRegitration
        fields = ['date_of_withdrawal','demanded_service','demand_Service_cashkind','estimated_cost','date_of_advance_payment','semister','year']
    
from dashboard.models import Course
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields= "__all__"



class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)