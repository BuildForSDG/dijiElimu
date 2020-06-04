from .models import Course, Unit, Video, Book, Department
from rest_framework import serializers
from users.serializers import UserSerializer
from subscription.serializers import SubscriptionSerializer


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        """Returns a list of all fields in model department"""
        model = Department
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    enrolled_students = UserSerializer(read_only=True, many=True)
    course = SubscriptionSerializer(read_only=True, many=True)

    class Meta:
        """Returns a list of all fields in model course"""
        model = Course
        fields = '__all__'

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related(
            'enrolled_students', 'tutor')
        return queryset


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
