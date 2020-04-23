from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurantUser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Restaurant(models.Model):
    restaurantName = models.CharField(max_length=100, verbose_name='restaurant Name')
    address = models.CharField(max_length=250)
    phone = PhoneField()
    url = models.URLField(max_length=200, verbose_name='URL')
    vanityURI = models.SlugField(
                max_length=100,
                verbose_name='Restaurant URI',
                unique=True,
                null=True,
                default=None
                )
    aboutUs = models.TextField(max_length=350, verbose_name='About Us')
    mealCost = models.IntegerField(verbose_name='Meal Cost')
    merchantID = models.CharField(max_length=100, verbose_name='PayPal Merchant ID')
    totalCollected = models.IntegerField(default=0)
    mealsDonated = models.IntegerField(default=0)
    goal = models.IntegerField(default=0, verbose_name='Weekly Meal Goal')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    lat = models.FloatField()
    lng = models.FloatField()

    def get_absolute_url(self):
        return reverse('rest_profile', kwargs={'restaurant_id': self.id})

class Transaction(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    mealNumber = models.IntegerField()
    dollarAmount = models.IntegerField()
    date = models.DateField("transaction date")

class Facility(models.Model):
    facilityName = models.CharField(max_length=100, verbose_name='facility Name')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    lat = models.FloatField()
    lng = models.FloatField()

class Logo(models.Model):
    url = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)