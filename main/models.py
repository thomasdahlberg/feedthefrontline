from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Restaurant(models.Model):
    restaurantName = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone = models.IntegerField()
    url = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)
    aboutUs = models.TextField()
    mealCost = models.IntegerField()
    totalCollected = models.IntegerField()
    mealsDonated = models.IntegerField()
    goal = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    lat = models.FloatField()
    lng = models.FloatField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'rest_id': self.id})

class Transaction(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    mealNumber = models.IntegerField()
    dollarAmount = models.IntegerField()
    date = models.DateField("transaction date")

class Facility(models.Model):
    facilityName = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    active = models.BooleanField()
    lat = models.FloatField()
    lng = models.FloatField()
