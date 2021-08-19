from django.contrib import admin
from .models import UserModel, UserBook
# Register your models here.

admin.site.register(UserModel)
admin.site.register(UserBook)