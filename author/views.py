from book.models import BookModel
from book.serializers import BookSearchSerializer, BookSerializer
from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import NotFound

from .models import AuthorModel
from .serializers import AuthorSearchSerializer, AuthorSerializer


class AuthorListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer

    def get_queryset(self):
        author = generics.get_object_or_404(AuthorModel, id=self.kwargs.get('pk'))
        queryset = BookModel.objects.filter(author=author)
        return queryset


class AuthorSearchView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AuthorSearchSerializer

    def get_queryset(self):
        qs = AuthorModel.objects.filter(fullname=self.kwargs.get('fullname'))
        if qs:
            return qs
        else:
            raise NotFound()
