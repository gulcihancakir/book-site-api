from django.contrib import admin
from .models import BookModel, TypeOfBookModel

admin.site.register(BookModel)
admin.site.register(TypeOfBookModel)