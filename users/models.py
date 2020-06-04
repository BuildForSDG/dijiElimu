from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """model for User."""

    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(
        verbose_name='username', max_length=100, blank=True, unique=True)
    first_name = models.CharField(verbose_name='first name', max_length=100)
    last_name = models.CharField(verbose_name='last name', max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    photo = models.ImageField(upload_to='users/photos',
                              default='useravatar.png')
    education_level = models.CharField(
        verbose_name='education level', max_length=100, null=True)
    designation = models.CharField(blank=True, max_length=100)
    expertise = models.CharField(
        blank=True, max_length=255, verbose_name='expert_in')
    stripe_user_id = models.CharField(max_length=255, blank=True)
    stripe_access_token = models.CharField(max_length=255, blank=True)
    joining_date = models.DateField(auto_now_add=True)
    registration_number = models.CharField(
        max_length=6, null=True, unique=True)
    guardian_mobile = models.CharField(max_length=11, blank=True, null=True)
    is_seller = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
