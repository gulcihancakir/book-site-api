from account.models import UserModel
from book.models import BookModel
from django.db import models


class QuotationModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(BookModel, on_delete=models.DO_NOTHING)
    quotation = models.CharField(max_length=500)
    quotation_page = models.IntegerField(null=True, blank=True)
    published_date = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=[
                                    'book', 'quotation_page', 'quotation'], name='same_book_quotation_constraints')
        ]


class RequotationModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    quotation = models.ForeignKey(QuotationModel, on_delete=models.DO_NOTHING)
