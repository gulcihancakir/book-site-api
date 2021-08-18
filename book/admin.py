from django.contrib import admin
from .models import BookModel, TypeOfBookModel,ReadingListModel

admin.site.register(BookModel)
admin.site.register(TypeOfBookModel)
admin.site.register(ReadingListModel)