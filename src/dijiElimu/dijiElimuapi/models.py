from django.db import models

from embed_video.fields import EmbedVideoField


class Student(models.Model):
    gender = (
        ('Select', 'Select'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    student_id = models.AutoField(primary_key=True,)
    first_name = models.CharField(verbose_name='first name', max_length=100)
    second_name = models.CharField(verbose_name='second name', max_length=100)
    user_name = models.CharField(verbose_name='user name', max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    year = models.IntegerField()
    createdAt = models.DateField(auto_now_add=True)
    sex = models.CharField(default='Select', choices=gender, max_length=100)
    phone_number = models.CharField(verbose_name='phone number', max_length=10)
    major = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.first_name}, {self.second_name}, {self.user_name}'

class Tutor(models.Model):
    tutor_id = models.AutoField(primary_key=True,)
    first_name = models.CharField(verbose_name='first name', max_length=100)
    second_name = models.CharField(verbose_name='second name', max_length=100)
    user_name = models.CharField(verbose_name='user name', max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(verbose_name='phone number', max_length=10)
    major = models.CharField(max_length=100)
    createdAt = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.first_name}, {self.second_name}, {self.user_name}'

class Major(models.Model):
    major_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    available = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'major'

    def __str__(self):
        return self.title

class Unit(models.Model):
    unit_name = models.CharField(verbose_name='unit name', max_length=100)
    unit_code = models.IntegerField(verbose_name='unit code')
    student = models.ManyToManyField('Student')
    video_url = EmbedVideoField()
    video_id = models.CharField(blank=False, max_length=32)
    file_name = models.CharField(max_length=500)
    Tutor = models.CharField(max_length=100)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.unit_name


class Grade(models.Model):
    unit_title = models.CharField(verbose_name='unit title', max_length=100)
    unit_code = models.IntegerField()
    student = models.CharField(max_length=100)
    grade_type = models.CharField(verbose_name='grade', max_length=1)
    grade_mark = models.IntegerField(verbose_name='grade mark')

    def __str__(self):
        return self.grade_type

class Semester(models.Model):
    names = (
        ('Select', 'Select'),
        ('One', 'One'),
        ('Two', 'Two'),
        ('Three', 'Three'),
    )
    semester_id = models.IntegerField()
    semester_name = models.CharField(verbose_name='semester name', default='Select', choices=names, max_length=100)

    class Meta:
        verbose_name_plural = 'semester'

    def __str__(self):
        return self.semester_name

class Attendance(models.Model):
    unit = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    student = models.ManyToManyField(Student)
    tutor = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Attendance'

    def __str__(self):
        return self.unit
