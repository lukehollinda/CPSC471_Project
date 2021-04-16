from django.shortcuts import render

from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by('name')
    serializer_class = CitySerializer

class NeighborhoodViewSet(viewsets.ModelViewSet):
    queryset = Neighborhood.objects.all().order_by('name')
    serializer_class = NeighborhoodSerializer

class LandViewSet(viewsets.ModelViewSet):
    queryset = Land.objects.all().order_by('address')
    serializer_class = LandSerializer

class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all().order_by('companyName')
    serializer_class = DeveloperSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all().order_by('ownerId')
    serializer_class = OwnerSerializer

class PersonOwnerViewSet(viewsets.ModelViewSet):
    queryset = PersonOwner.objects.all().order_by('ownerId')
    serializer_class = PersonOwnerSerializer

class CompanyOwnerViewSet(viewsets.ModelViewSet):
    queryset = CompanyOwner.objects.all().order_by('ownerId')
    serializer_class = CompanyOwnerSerializer

class BankOwnerViewSet(viewsets.ModelViewSet):
    queryset = BankOwner.objects.all().order_by('ownerId')
    serializer_class = BankOwnerSerializer

class OwnsRelationViewSet(viewsets.ModelViewSet):
    queryset = OwnsRelation.objects.all().order_by('ownerId')
    serializer_class = OwnsRelationSerializer

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all().order_by('land')
    serializer_class = BuildingSerializer

class CommecialBuildingViewSet(viewsets.ModelViewSet):
    queryset = CommercialBuilding.objects.all().order_by('building')
    serializer_class = CommercialBuildingSerializer

class ResidentialBuildingViewSet(viewsets.ModelViewSet):
    queryset = ResidentialBuilding.objects.all().order_by('building')
    serializer_class = ResidentialBuildingSerializer

class RenterViewSet(viewsets.ModelViewSet):
    queryset = Renter.objects.all().order_by('renterId')
    serializer_class = RenterSerializer