from django.shortcuts import render
from rest_framework import viewsets
from .models import User, School, DataSubmission, ConnectivityImpact
from .serializers import UserSerializer, SchoolSerializer, DataSubmissionSerializer, ConnectivityImpactSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class DataSubmissionViewSet(viewsets.ModelViewSet):
    queryset = DataSubmission.objects.all()
    serializer_class = DataSubmissionSerializer

class ConnectivityImpactViewSet(viewsets.ModelViewSet):
    queryset = ConnectivityImpact.objects.all()
    serializer_class = ConnectivityImpactSerializer

