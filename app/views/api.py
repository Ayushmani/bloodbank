# import libraries
from rest_framework import generics

# import models
from app.models import BloodGroup

# import serializers
from app.serializers import BloodGroupSerializer

class ApiListBloodGroup(generics.ListCreateAPIView):
    queryset = BloodGroup.objects.all()
    serializer_class = BloodGroupSerializer

class ApiUpdateDeleteBloodGroup(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloodGroup.objects.all()
    serializer_class = BloodGroupSerializer
