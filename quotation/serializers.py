import quotation
from book.models import BookModel
from rest_framework import serializers
from .models import QuotationModel
from book.serializers import BookSerializer

class QuotationSerializer(serializers.ModelSerializer):
    book = BookSerializer()
 
    class Meta:
        model = QuotationModel
        fields = ['title', 'quotation', 'book']





    