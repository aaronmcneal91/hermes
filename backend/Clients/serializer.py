from .models import Client
from Client_Type.models import Client_Type
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name','email', 'address', 'type', 'type_id' )
        depth = 1
    type_id = serializers.IntegerField(write_only=True)

