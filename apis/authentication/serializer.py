from rest_framework import serializers
from . import models

class User_Authentication_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.User_Authentication
        fields = '__all__'
        