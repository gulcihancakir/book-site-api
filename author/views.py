from .models import AuthorModel
from .serializers import AuthorSerializer
from rest_framework import generics

class AuthorListView(generics.ListCreateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer