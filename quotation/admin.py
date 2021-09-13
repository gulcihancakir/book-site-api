from django.contrib import admin

from .models import QuotationModel, RequotationModel

# Register your models here.

admin.site.register(QuotationModel)
admin.site.register(RequotationModel)
