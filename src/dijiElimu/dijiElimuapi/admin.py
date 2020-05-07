from django.contrib import admin

from .models import Student, Tutor, Major, Unit, Grade, Semester, Attendance

# Register your models here.
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(Major)
admin.site.register(Unit)
admin.site.register(Grade)
admin.site.register(Semester)
admin.site.register(Attendance)
