from rest_framework import serializers
from .models import Client_Type

class ClientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_Type
        fields = [ 'id', 'type']