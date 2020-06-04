from rest_framework import serializers
from rest_framework.authtoken.models import Token
from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from .models import User


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'email', 
            'first_name',
            'last_name ',
            'date_of_birth',
            'mobile',  
            'photo',
            'joining_date', 
            'registration_number',
            'guardian_mobile',
            'is_student'
        )


class TutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name ',
            'date_of_birth',
            'mobile',  
            'photo',
            'education_level',
            'designation',
            'expertise',
            'joining_date',
            'is_tutor'
        )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'is_tutor',
            'is_student'
        )


class UserRegisterSerializer(RegisterSerializer):
    """serializer for UserRegisterSerializer."""

    class Meta:
        model = User
        fields = '__all__'

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'date_of_birth': self.validated_data.get(
                'date_of_birth', ''),
            'mobile': self.validated_data.get('mobile', ''),
            'education_level': self.validated_data.get(
                'education_level', ''),
            'expertise': self.validated_data.get('expertise', ''),
            'designation': self.validated_data.get('designation', ''),
            'registration_number': self.validated_data.get(
                'registration_number', ''),
            'is_tutor': self.validated_data.get('is_tutor', ''),
            'is_seller': self.validated_data.get('is_seller', ''),
            'is_student': self.validated_data.get('is_student', ''),
            'joining_date': self.validated_data.get('joining_date', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.is_student = self.cleaned_data.get('is_student')
        user.is_teacher = self.cleaned_data.get('is_teacher')
        user.save()
        adapter.save_user(request, user, self)
        return user


class TokenSerializer(serializers.ModelSerializer):
    """docstriustomTokenSerializer."""
    auth_user = serializers.SerializerMethodField()

    class Meta:
        model = Token
        fields = '__all__'

    def get_auth_user(self, obj):
        serializer_data = UserSerializer(
            obj.user
        ).data
        return serializer_data
