from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    phone = models.CharField(max_length=15,unique=True,blank=False,null=False)

    dob = models.DateField(blank=False,null=False)

