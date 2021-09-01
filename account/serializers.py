from book.models import ReadingListModel
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserModel


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class UserRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserModel
        fields = ['id', 'user', 'gender', 'birth_date', 'picture']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        validated_data['user'] = user
        usermodel = UserModel.objects.create(**validated_data)
        return usermodel


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingListModel
        fields = ['user', 'book']


class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class UserModelDetailSearchSerializer(serializers.ModelSerializer):
    user = UserSearchSerializer()

    class Meta:
        model = UserModel
        fields = ['user', 'gender', 'birth_date', 'picture']
