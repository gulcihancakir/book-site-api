from .models import QuotationModel
from .serializers import QuotationSerializer
from rest_framework import generics


class QuotationView(generics.ListCreateAPIView):
    queryset = QuotationModel.objects.all()
    serializer_class = QuotationSerializer
