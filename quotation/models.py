from account.models import UserModel
from book.models import BookModel
from django.db import models


class QuotationModel(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    quotation = models.TextField()
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
