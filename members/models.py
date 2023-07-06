from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    REQUIRED_FIELDS = []
    email = None
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=50)