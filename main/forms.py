from django.forms import ModelForm
from .models import Restaurant

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'restaurantName',
            'address',
            'phone',
            'url',
            'logo',
            'aboutUs',
            'mealCost',
            'totalCollected',
            'goal',
            'lat',
            'lng'
            ]