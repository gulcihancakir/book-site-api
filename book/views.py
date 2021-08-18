from .models import ReadingListModel
from .serializers import ReadingListSerializer
from rest_framework import generics


class ReadingListView(generics.ListCreateAPIView):
    queryset = ReadingListModel.objects.all()
    serializer_class = ReadingListSerializer