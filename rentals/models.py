
# rentals/models.py

from django.db import models

class UAV(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    weight = models.FloatField()
    category = models.CharField(max_length=255)

    class Meta:
        app_label = 'rentals'
class User(models.Model):
    name = models.CharField(max_length=150)
    surname= models.CharField(max_length=150)
    email= models.CharField(max_length=250)
    createdDate = models.DateTimeField()
    password = models.CharField(max_length=250)
    
    class Meta:
        app_label = 'rentals'


class Rental(models.Model):
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    renting_member = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'rentals'

