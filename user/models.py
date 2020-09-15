from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    address_new = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
