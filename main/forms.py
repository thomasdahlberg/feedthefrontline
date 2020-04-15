from django.forms import ModelForm
from .models import Restaurant
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'restaurantName',
            'address',
            'phone',
            'url',
            'aboutUs',
            'mealCost',
            'goal',
            'lat',
            'lng'
            ]


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    restaurantUser = forms.BooleanField(label="Are you a restaurant?", required=False, initial=False)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'restaurantUser')
