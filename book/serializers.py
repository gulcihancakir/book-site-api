from django.db.models import fields
from rest_framework import serializers
from .models import BookModel, ReadingListModel, TypeOfBookModel, UserBook


class TypeOfBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfBookModel
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = BookModel
        fields = ['id', 'name', 'image', 'page_number',
                  'language', 'country', 'publisher', 'author']



class ReadingPostSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ReadingListModel
        fields = ['book']

class ReadingDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingListModel
        fields = ['user', 'book']

class ReadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBook
        fields = ['book', 'read_time', 'read', 'like', 'rate']

class ReadsDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBook
        fields = ['book', 'read_time', 'read', 'like', 'rate']

class BookSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'
