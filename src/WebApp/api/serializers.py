from rest_framework import serializers
from .models import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name', 'latitude', 'longitude')

class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ('name', 'cityName')

class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = ('address', 'postalCode', 'sqrAcres', "neighborhoodName")

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ('companyName', 'headQuarters')
    
class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('ownerId', 'email', 'phoneNumber')

class PersonOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonOwner
        fields = ('ownerId', 'firstName', 'middleName', 'lastName')

class CompanyOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyOwner
        fields = ('ownerId', 'companyName', 'companyType')
    
class BankOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankOwner
        fields = ('ownerId', 'bankName', 'headQuarters')

class OwnsRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnsRelation
        fields = ('ownerId', 'land')

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ('land', 'developer', 'squareFootage', 'numberOfStories')

class CommercialBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommercialBuilding
        fields = ('building', 'industryType', 'numberOfDesks')

class ResidentialBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentialBuilding
        fields = ('building', 'numberOfBathrooms', 'numberOfBedrooms')

class RenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renter
        fields = ('renterId', 'building', 'firstName', 'middleName', \
                    'lastName', 'phoneNumber', 'email', 'costPerMonth', 'leaseDuration' )    
