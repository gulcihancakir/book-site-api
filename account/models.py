from book.models import BookModel, ReadingListModel
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class UserModel(User):
    CHOICES = [(1, 'FEMALE'),
               (2, 'MALE')]
    gender = models.CharField(
        max_length=10, choices=CHOICES, null=True, blank=True)
    birthdate = models.DateField()
    readinglist = models.OneToOneField(
        ReadingListModel, on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    read = models.ManyToManyField(BookModel, blank=True)


class UserBook(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    book = models.OneToOneField(BookModel, on_delete=models.CASCADE)
    read_time = models.IntegerField()
    rating = models.IntegerField(default=0,
                                 validators=[
                                     MaxValueValidator(10),
                                     MinValueValidator(0)
                                 ])
    read = models.BooleanField(default=False)
