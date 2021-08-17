from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from author.models import AuthorModel

class TypeOfBookModel(models.Model):
    name = models.CharField(max_length=50)

class BookModel(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    typeofbook = models.ManyToManyField(TypeOfBookModel)
    rating = models.IntegerField(default=0, 
            validators=[
                MaxValueValidator(5),
                MinValueValidator(0)
    ])
    page_number = models.IntegerField()
    language = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)
    book_summary = models.TextField()


    
    


