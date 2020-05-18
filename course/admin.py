from django.contrib import admin

from .models import Department, Course, Unit, Video, Book

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Unit)
admin.site.register(Video)
admin.site.register(Book)

