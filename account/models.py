from django.db import models
from .managers import UserManger
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    user_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=225, unique=True)
    full_name = models.CharField(max_length=100)
    phone_nember = models.CharField(max_length=11, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManger()


    USERNAME_FIELD = "user_name"
    REQUIRED_FIELDS = ["user_name", "email", "full_name"]

    def __str__(self):
        return self.full_name


    @property
    def is_staff(self):
        return self.is_admin    