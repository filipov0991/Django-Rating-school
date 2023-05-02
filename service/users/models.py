from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    school = models.CharField(max_length=100, unique=False)