# import libraries
from rest_framework import generics

# import models
from app.models import BloodGroup
from app.models import Individual

# import serializers
from app.serializers import BloodGroupSerializer
from app.serializers import IndividualSerializer

class ApiListBloodGroup(generics.ListCreateAPIView):
    queryset = BloodGroup.objects.all()
    serializer_class = BloodGroupSerializer

class ApiUpdateDeleteBloodGroup(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloodGroup.objects.all()
    serializer_class = BloodGroupSerializer

class ApiListIndividual(generics.ListCreateAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer

class ApiUpdateDeleteIndividual(generics.RetrieveUpdateDestroyAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer
