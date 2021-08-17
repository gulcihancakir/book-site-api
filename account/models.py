
from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser

class UserModel(User):
    CHOICES = [(1,'FEMALE'),
               (2,'MALE')]
    gender = models.CharField(max_length=2,choices=CHOICES)
    birtdate = models.DateField()
  


