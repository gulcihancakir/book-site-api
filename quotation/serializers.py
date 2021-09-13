import quotation
from account.serializers import UserRegisterSerializer
from book.models import BookModel
from book.serializers import BookSerializer
from rest_framework import serializers

from .models import QuotationModel, RequotationModel

class QuotationSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    class Meta:
        model = QuotationModel
        fields = ['user', 'book', 'quotation', 'quotation_page', 'published_date']

class QuotationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationModel
        fields = ['book', 'quotation', 'quotation_page']

class RequotationListSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer()
    quotation = QuotationSerializer()

    class Meta:
        model = RequotationModel
        fields = ['user', 'quotation']


class RequotationPostSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = RequotationModel
        fields = ['user', 'quotation']