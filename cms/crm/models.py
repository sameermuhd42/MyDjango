from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustUser(AbstractUser):
    age = models.CharField(max_length=255)
