from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Restaurant, Transaction, Facility
from .forms import RestaurantForm

import googlemaps

gmaps = googlemaps.Client(key = 'AIzaSyDoVTW1-BZU-gfpY86X4FRKoc6hy8Oa67I')

# Google Maps/Places APIs
# def place_search(request):
#     search_text = request.places-search
#     places = gmaps.find_place(search_text)
#     return render(request, 'test.html', { 'places': places })

# Create your views here.
def home(request):
    return render(request, 'home.html')

def test(request):
    rest_form = RestaurantForm()
    return render(request, 'test.html', { 'rest_form': rest_form })

# Authorization and Registration

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# Restuarant Views (Visitor Visible)

def rest_index(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/index.html', { 'restaurants' : restaurants })

def rest_profile(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    return render(request, 'restaurants/detail.html', { 'restaurant': restaurant })

# Restaurant Owner Views

def assoc_fac(request, rest_id, fac_id):
    pass

def rm_fac(request, rest_id, fac_id):
    pass

def upload_logo(request, rest_id):
    pass

class RestCreate(CreateView):
    model = Restaurant
    fields = [
        'restaurantName',
        'address',
        'phone',
        'url',
        'logo',
        'aboutUs',
        'mealCost',
        'goal',
    ]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class RestUpdate(UpdateView):
    model = Restaurant
    fields = [
        'restaurantName',
        'address',
        'phone',
        'url',
        'logo',
        'aboutUs',
        'mealCost',
        'goal',
    ]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class RestDelete(DeleteView):
    model = Restaurant
    success_url = '/restaurants/'