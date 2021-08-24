from django.contrib.auth.models import User
from django.db import models


class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    picture = models.ImageField(null=True, blank=True)
    CHOICES = [(1, 'FEMALE'),
               (2, 'MALE')]
    gender = models.IntegerField(choices=CHOICES)
