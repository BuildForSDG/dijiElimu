from rest_framework import viewsets

from .models import User
from .serializers import (
    UserSerializer,
    StudentSerializer,
    TutorSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = User.objects.filter(is_student=True)


class TutorViewSet(viewsets.ModelViewSet):
    serializer_class = TutorSerializer
    queryset = User.objects.filter(is_tutor=True)
