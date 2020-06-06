from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField


class Unit(models.Model):
    unit_name = models.CharField(verbose_name='unit name', max_length=100)
    unit_code = models.IntegerField(
        verbose_name='unit code', default=0, unique=True)
    student = models.CharField(max_length=100)
    video_url = EmbedVideoField()
    video_id = models.CharField(blank=False, max_length=32)
    file_name = models.CharField(max_length=500)
    Tutor = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        """'return formatted string"""
        return self.unit_name


class Course(models.Model):
    course_name = models.CharField(
        verbose_name='course name', max_length=100, unique=True)
    units = models.ManyToManyField(Unit)
    course_code = models.IntegerField(
        verbose_name='course code', default=0, unique=True)
    approved = models.BooleanField(default=False)
    published_date = models.DateTimeField(
        verbose_name='published date', default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(
        upload_to='images', null=True)
    blog = models.TextField(
        max_length=500,
        default="""Hundreds of teachers
        have gone through our system and
        become qualified teachers of information
        technology. Study with us today""")
    price = models.DecimalField(
        max_digits=8, decimal_places=2, default=0.00)
    fee = models.DecimalField(
        max_digits=8, decimal_places=2, default=0.00)
    enrolled_students = models.ManyToManyField(
        'users.User', through='subscription.Subscription'
    )
    tutor = models.ManyToManyField(
        'users.User',
        related_name='courses_asigned'
    )

    @staticmethod
    def unsubscribe(current_user, course):
        course.enrolled_students.remove(current_user)

    def __str__(self):
        """'return formatted string"""
        return self.course_name


class Department(models.Model):
    title = models.CharField(max_length=100)
    department_code = models.IntegerField(
        verbose_name='department name', default=0, unique=True)
    blog = models.TextField(
        max_length=500,
        default="""Hundreds of teachers have gone
        through our system and become qualified
        teachers of information technology. Study with us today""")
    course = models.ManyToManyField(Course)

    def __str__(self):
        """'return formatted string"""
        return self.title


class Video(models.Model):
    code = models.IntegerField(unique=True)
    unit_title = models.CharField(max_length=100)
    video_url = EmbedVideoField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    uploadedAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now_add=True)

    def __str__(self):
        """'return formatted string"""
        return self.unit_title


class Book(models.Model):
    book_title = models.CharField(verbose_name='book title', max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='documents')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    uploadedAt = models.DateField(default=timezone.now)
    updatedAt = models.DateField(default=timezone.now)

    def __str__(self):
        """'return formatted string"""
        return self.book_title
