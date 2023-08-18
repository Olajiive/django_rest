from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = (
            'id',
            'username',
            'password',
            'email'
        )

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'name', 
            'age',
            'occupation'
        )