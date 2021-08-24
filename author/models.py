from django.db import models

class AuthorModel(models.Model):
    fullname = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)
    unvan = models.CharField(max_length=250)
    birth = models.CharField(max_length=250)
    death = models.CharField(max_length=250)
    life = models.TextField()
    

    def __str__(self):
        return self.fullname 