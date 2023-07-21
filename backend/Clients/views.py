from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from .models import Client
from Client_Type.models import Client_Type
from .serializer import ClientSerializer
from django.contrib.auth.models import User
from Client_Type.serializer import ClientTypeSerializer 


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_clients(request):
    clients = Client.objects.all()
    if request.method == 'GET':
        serializer = ClientSerializer(clients, many = True)
        return Response (serializer.data)
    elif request.method == 'POST':
        serializer = ClientSerializer(data = request.data)
        serializer.is_valid()
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)