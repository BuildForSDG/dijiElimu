from .models import Course, Unit, Video, Book, Department
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        """Returns a list of all fields in model department"""
        model = Department
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        """Returns a list of all fields in model course"""
        model = Course
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        """Returns a list of all fields in model unit"""
        model = Unit
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        """Returns a list of all fields in model video"""
        model = Video
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        """Returns a list of all fields in model book"""
        model = Book
        fields = '__all__'
