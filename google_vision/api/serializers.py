from rest_framework import serializers
from google_vision.models import GoogleVision

class GoogleVisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleVision
        fields = '__all__'
