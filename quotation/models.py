from account.models import UserModel
from book.models import BookModel
from django.db import models


class QuotationModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(BookModel, on_delete=models.DO_NOTHING)
    quotation = models.TextField()
    quotation_page = models.IntegerField(null=True, blank=True)
    published_date = models.DateTimeField()
