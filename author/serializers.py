from rest_framework import serializers

from .models import AuthorModel


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ['fullname', 'unvan', 'birth', 'death', 'life']


class AuthorSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'
