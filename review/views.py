from account.permissions import IsOwner
from account.models import UserModel
from rest_framework import permissions
from .models import ReviewModel
from .serializers import ReviewPostSerializer, ReviewSerializer
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class ReviewView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, ]
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, ]
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewPostSerializer


class ReviewPostView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [SessionAuthentication, ]
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewPostSerializer

    def perform_create(self, serializer):
        user = UserModel.objects.get(user__username=self.request.user)
        serializer.save(user=user)


class ReviewUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    authentication_classes = [SessionAuthentication, ]
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewPostSerializer
