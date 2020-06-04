from rest_framework import viewsets
from .serializers import (
    DepartmentSerializer,
    CourseSerializer,
    UnitSerializer,
    VideoSerializer,
    BookSerializer
)

from .models import Department, Course, Unit, Video, Book


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    queryset = CourseSerializer.setup_eager_loading(queryset=queryset)


class UnitViewSet(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()


class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
