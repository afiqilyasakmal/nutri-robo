from django.db import models
from django.contrib.auth.models import User

GENDER = [('Male', 'Male'), ('Female', 'Female')]
ROLE = [('User', 'User'), ('Instructor', 'Instructor')]

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True) 
    email = models.CharField(max_length=50, null=True)
    role = models.CharField(max_length=20, choices=ROLE, default='User')
    

class PhysicalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    gender = models.CharField(max_length=20, choices=GENDER,default='Male') 
    weight = models.FloatField()
    height = models.FloatField()
    age = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    calories = models.FloatField()
    water = models.IntegerField()
    sleep = models.CharField(max_length=20)
    exercise = models.IntegerField()
