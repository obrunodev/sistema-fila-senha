from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True)
