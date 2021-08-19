from rest_framework import generics

from .models import UserModel
from .serializers import UserDetailSerializer, UserRegisterSerializer


class UserRegisterView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserRegisterSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserDetailSerializer