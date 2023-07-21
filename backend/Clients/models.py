from django.db import models
from Client_Type.models import Client_Type

class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    type = models.ForeignKey(Client_Type, on_delete=models.CASCADE)
        
    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
