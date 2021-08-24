from rest_framework import serializers
from .models import BookModel, ReadingListModel, TypeOfBookModel


class TypeOfBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfBookModel
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    typeofbook = TypeOfBookSerializer(many=True, read_only=True)

    class Meta:
        model = BookModel
        fields = ['name', 'image', 'page_number',
                  'language', 'country', 'publisher', 'typeofbook', 'author']


class ReadingListSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True, read_only=True)

    class Meta:
        model = ReadingListModel
        fields = ['book']
