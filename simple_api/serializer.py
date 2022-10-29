from dataclasses import field
from re import M
from rest_framework import serializers

from . models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        field =('id','name','language','price')
