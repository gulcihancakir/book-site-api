from django.contrib import admin

from .models import (BookModel, CountryModel, LanguageModel, PublisherModel,
                     ReadingListModel, TypeModel, TypeOfBookModel, UserBook)

admin.site.register(BookModel)
admin.site.register(TypeOfBookModel)
admin.site.register(CountryModel)
admin.site.register(LanguageModel)
admin.site.register(PublisherModel)
admin.site.register(TypeModel)
admin.site.register(ReadingListModel)
admin.site.register(UserBook)
