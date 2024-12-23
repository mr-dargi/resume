from django.db import models
from .managers import UserManger
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=225, unique=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManger()


    USERNAME_FIELD = "user_name"
    REQUIRED_FIELDS = ["email", "full_name", "phone_number"]

    def __str__(self):
        return self.full_name


    @property
    def is_staff(self):
        return self.is_admin    
