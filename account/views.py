from book.models import ReadingListModel, UserBook
from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from .models import UserModel
from .serializers import (UserModelDetailSearchSerializer, UserDetailSerializer,
                          UserRegisterSerializer)


class UserRegisterView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserRegisterSerializer


class UserReadingListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, ]
    serializer_class = UserDetailSerializer

    def get_queryset(self):
        user = self.request.user
        print(user)
        qs = ReadingListModel.objects.filter(user_id=self.kwargs.get('pk'))
        print(qs)
        if qs:
            return qs
        else:
            raise NotFound()


class UserReadsListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, ]
    serializer_class = UserDetailSerializer

    def get_queryset(self):
        qs = UserBook.objects.filter(read='True').filter(
            user=self.kwargs.get('pk'))
        if qs:
            return qs
        else:
            raise NotFound()


class UserSearchView(generics.ListAPIView):  
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, ]
    serializer_class = UserModelDetailSearchSerializer

    def get_queryset(self):
        qs = UserModel.objects.filter(
            user__username=self.kwargs.get('username'))
        if qs:
            return qs
        else:
            raise NotFound()
