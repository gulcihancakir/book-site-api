from account.models import UserModel
from account.permissions import IsOwner
from django.http import request
from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from book.serializers import (BookSearchSerializer, BookSerializer,
                              ReadingDeleteSerializer, ReadingPostSerializer,
                              ReadsDeleteSerializer, ReadsSerializer)

from .models import BookModel, ReadingListModel, UserBook


class BookListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, ]

    queryset = BookModel.objects.all()
    serializer_class = BookSerializer


class ReadingPostView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, ]
    queryset = ReadingListModel.objects.all()
    serializer_class = ReadingPostSerializer

    def perform_create(self, serializer):
        user = UserModel.objects.get(user=self.request.user.id)
        serializer.save(user=user)


class ReadingListDeleteView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    authentication_classes = [SessionAuthentication, ]
    queryset = ReadingListModel.objects.all()
    serializer_class = ReadingDeleteSerializer


class ReadsPostView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, ]
    queryset = UserBook.objects.all()
    serializer_class = ReadsSerializer

    def perform_create(self, serializer):
        user = UserModel.objects.get(user=self.request.user.id)
        serializer.save(user=user)


class ReadsDeleteView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    authentication_classes = [SessionAuthentication, ]
    queryset = UserBook.objects.all()
    serializer_class = ReadsDeleteSerializer


class BookSearchView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookSearchSerializer

    def get_queryset(self):
        qs = BookModel.objects.filter(name=self.kwargs.get('name'))
        print("user", qs)
        if qs:
            return qs
        else:
            raise NotFound()
