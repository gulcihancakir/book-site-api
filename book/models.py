from django.db.models.fields import IntegerField
from account.models import UserModel
from author.models import AuthorModel
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CountryModel(models.Model):
    name = models.CharField(max_length=100)


class LanguageModel(models.Model):
    name = models.CharField(max_length=100)


class PublisherModel(models.Model):
    name = models.CharField(max_length=250)


class BookModel(models.Model):
    author = models.ForeignKey(AuthorModel, on_delete=models.DO_NOTHING)
    language = models.ForeignKey(LanguageModel, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(CountryModel, on_delete=models.DO_NOTHING)
    publisher = models.ForeignKey(PublisherModel, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)
    page_number = models.IntegerField()
    material = models.CharField(max_length=100)
    date = models.DateTimeField()
    book_summary = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'publisher', 'name'], name='same_book_bookmodel_constraints')
        ]


class TypeModel(models.Model):
    name = models.CharField(max_length=100)


class TypeOfBookModel(models.Model):
    type = models.ForeignKey(TypeModel, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(BookModel, on_delete=models.DO_NOTHING)


class ReadingListModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(BookModel, on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['book', 'user'], name='same_book_readinglistmodel_constraints')
        ]


class UserBook(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(BookModel, on_delete=models.DO_NOTHING)
    read_time = models.IntegerField(null=True, blank=True)
    read = models.BooleanField(default=False)
    like = models.BooleanField(default=False)
    rate = IntegerField(default=0, validators=[
                        MaxValueValidator(10), MinValueValidator(0)])
