from django.shortcuts import render

from rest_framework import viewsets
from .serializers import LandSerializer
from .models import Land

# Create your views here.

class LandViewSet(viewsets.ModelViewSet):
    queryset = Land.objects.all().order_by('address')
    serializer_class = LandSerializer