from rest_framework import serializers

from .models import ReviewModel

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReviewModel
        fields = ['user','book', 'review', 'published_date']

class ReviewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ['review', 'book']
    

    