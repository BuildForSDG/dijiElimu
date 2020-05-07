from rest_framework import viewsets
from dijiElimu.api.serializers import StudentSerializer, TutorSerializer, MajorSerializer, UnitSerializer, GradeSerializer, SemesterSerializer, AttendanceSerializer
from .models import Student, Tutor, Major, Unit, Grade, Semester, Attendance

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class TutorViewSet(viewsets.ModelViewSet):
    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()

class MajorViewSet(viewsets.ModelViewSet):
    serializer_class = MajorSerializer
    queryset = Major.objects.all()

class UnitViewSet(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

class GradeViewSet(viewsets.ModelViewSet):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()

class SemesterViewSet(viewsets.ModelViewSet):
    serializer_class = SemesterSerializer
    queryset = Semester.objects.all()

class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()
