from account.models import UserModel
from book.models import BookModel
from django.db import models


class ReviewModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(BookModel, on_delete=models.DO_NOTHING)
    review = models.CharField(max_length=500)

    published_date = models.DateTimeField(auto_now=True) 
