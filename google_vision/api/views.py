from rest_framework import viewsets
from google_vision.models import GoogleVision
from .serializers import GoogleVisionSerializer


class GoogleVisionViewSet(viewsets.ModelViewSet):
    queryset = GoogleVision.objects.all()
    serializer_class = GoogleVisionSerializer
