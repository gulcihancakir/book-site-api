from book.models import BookModel
from book.serializers import BookSerializer
from rest_framework import serializers

from .models import QuotationModel


class QuotationSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = QuotationModel
        fields = ['title', 'quotation', 'book', 'user', 'quotation_page_number']

    def create(self, validated_data):
        book_data = validated_data.pop('book')
        book = BookModel.objects.create(**book_data)
        validated_data['book'] = book
        quotation = QuotationModel.objects.create(**validated_data)
        return quotation