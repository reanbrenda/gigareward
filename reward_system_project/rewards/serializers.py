# rewards/serializers.py
from rest_framework import serializers
from .models import User, School, DataSubmission, ConnectivityImpact

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class DataSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSubmission
        fields = '__all__'

class ConnectivityImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectivityImpact
        fields = '__all__'
