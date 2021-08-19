from .models import QuotationModel
from .serializers import QuotationSerializer
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class QuotationView(generics.ListAPIView):
    
    queryset = QuotationModel.objects.all()
    serializer_class = QuotationSerializer


class QuotationPostView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [SessionAuthentication, ]
    queryset = QuotationModel.objects.all()
    serializer_class = QuotationSerializer
