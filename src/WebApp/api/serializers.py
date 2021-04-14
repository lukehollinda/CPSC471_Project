from rest_framework import serializers
from .models import Land


class LandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Land
        fields = ('id', 'address', 'postalCode', 'sqrAcres')
