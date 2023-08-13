# rewards/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    points = models.PositiveIntegerField(default=0)

class School(models.Model):
    name = models.CharField(max_length=200)
    location = models.PointField()
    connectivity_status = models.BooleanField(default=False)

class DataSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

class ConnectivityImpact(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    impact_date = models.DateTimeField(auto_now_add=True)
