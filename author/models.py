from django.db import models

class AuthorModel(models.Model):
    fullname = models.CharField(max_length=100)
    unvan = models.CharField(max_length=100)
    birth = models.CharField(max_length=100)
    death = models.CharField(max_length=100)
    life = models.TextField()
    

    def __str__(self):
        return self.fullname 