from account.models import UserModel
from account.permissions import IsOwner
from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import QuotationModel, RequotationModel
from .serializers import QuotationPostSerializer, QuotationSerializer, RequotationListSerializer, RequotationPostSerializer


class QuotationView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, ]

    queryset = QuotationModel.objects.all()
    serializer_class = QuotationSerializer


class QuotationPostView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [SessionAuthentication, ]
    queryset = QuotationModel.objects.all()
    serializer_class = QuotationPostSerializer

    def perform_create(self, serializer):
        user = UserModel.objects.get(user__username=self.request.user)
        serializer.save(user=user)


class QuotationDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, ]
    queryset = QuotationModel.objects.all()
    serializer_class = QuotationPostSerializer


class QuotationUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    authentication_classes = [SessionAuthentication, ]
    queryset = QuotationModel.objects.all()
    serializer_class = QuotationPostSerializer

class RequotationView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, ]
    queryset = RequotationModel.objects.all()
    serializer_class = RequotationListSerializer

class RequotationPostView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [SessionAuthentication, ]
    queryset = RequotationModel.objects.all()
    serializer_class = RequotationPostSerializer

    def perform_create(self, serializer):
        user = UserModel.objects.get(user__username=self.request.user)
        serializer.save(user=user)