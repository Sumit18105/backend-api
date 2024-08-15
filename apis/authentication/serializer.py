from rest_framework import serializers
from . import models

class User_Authentication_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.User_Authentication
        fields = '__all__'
class Doctor_Authentication_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor_Authentication
        fields = '__all__'

class Accounts_Details_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Accounts_Details
        fields = '__all__'