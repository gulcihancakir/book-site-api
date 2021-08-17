from django.db import models

class AuthorModel(models.Model):
    unvan = models.CharField(max_length=100)
    birth = models.CharField(max_length=100)
    death = models.CharField(max_length=100)
    life = models.TextField()
