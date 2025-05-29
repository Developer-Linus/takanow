from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUser


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('landlord', 'Landlord'),
        ('agent', 'Agent'),
        ('collector', 'Collector'),
        ('admin', 'Admin')
    ]
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default='landlord')
    phone = PhoneNumberField(region='KE', unique=True, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'role', 'phone', 'location']

    objects = CustomUser()

    def __str__(self):
        return self.email
