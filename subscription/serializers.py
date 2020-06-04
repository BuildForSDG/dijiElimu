from rest_framework import serializers
from .models import Subscription
from course.models import Course
from users.models import User


class SubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=User.objects.all(), required=True)
    course = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Course.objects.all(), required=True)
    subscribed_course = serializers.SerializerMethodField()
    pending_balance = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = '__all__'

    def get_subscribed_course(self, obj):
        """
        Get users subscriptions from many to many retaionships
        """
        course = Course.objects.get(id=obj.course_id)
        return {
            'id': course.id,
            'name': course.course_name,
            'price': course.price
        }

    def get_pending_balance(self, obj):
        """
        Get pending balance on a course after subscription payment
        """
        course = Course.objects.get(id=obj.course.id)
        return course.price - obj.amount_paid
