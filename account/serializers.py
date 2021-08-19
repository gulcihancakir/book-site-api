from book.serializers import ReadingListSerializer
from .models import UserModel
from rest_framework import serializers

# Serializers define the API representation.


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'})

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password', 'gender', 'birthdate']


class UserDetailSerializer(serializers.ModelSerializer):
    readinglist=ReadingListSerializer()
    class Meta:
        model = UserModel
        fields = ['read', 'readinglist']

    