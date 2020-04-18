from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import RestaurantForm, SignUpForm

from .models import Restaurant, Transaction, Facility, Profile, Logo

from django.contrib.auth import login, authenticate

from .forms import SignUpForm

import uuid
import boto3
import googlemaps

API_KEY = 'AIzaSyCSoVHw83uV_E-uSqxMW7nTxuT4OQCL2m4'
S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'feedthefrontline'


# Create your views here.
def home(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')

# Authorization and Registration

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.restaurantUser = form.cleaned_data.get('restaurantUser')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            print(user.profile.restaurantUser)
            if user.profile.restaurantUser:
                login(request, user)
                return redirect('rest_create')
            else:
                login(request, user)
                return redirect('rest_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = SignUpForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# Restarant Views (Visitor Visible)

def rest_index(request):
    restaurants = Restaurant.objects.all().order_by('-id')
    facilities = Facility.objects.all().order_by('-id')
    rest_max = restaurants[0].id
    fac_max = facilities[0].id
    context = { 'restaurants': restaurants, 'facilities': facilities, 'rest_max': rest_max, "fac_max": fac_max }
    return render(request, 'restaurants/index.html', context)

def rest_profile(request, restaurant_id):
    error_message = ''
    restaurant = Restaurant.objects.get(id=restaurant_id)
    rest_facs = restaurant.facility_set.all()
    logo = restaurant.logo_set.all()
    print(rest_facs.values('id'))
    if request.method == 'POST':
        if request.POST['router'] == "1":
            print(request)
            gmaps = googlemaps.Client(key=API_KEY)
            search_text = request.POST['placestext']
            result = gmaps.places(query=search_text)
            facilities = result['results']
            context = {'restaurant':restaurant, 'error_message': error_message, 'facilities': facilities}
            return render(request, 'restaurants/detail.html', context)
    return render(request, 'restaurants/detail.html', { 'restaurant': restaurant, 'rest_facs': rest_facs, 'logo': logo })

def rest_create(request):
    error_message = ''
    if request.method == 'POST':
        if request.POST['router'] == "1":
            gmaps = googlemaps.Client(key=API_KEY)
            search_text = request.POST['placestext']
            result = gmaps.places(query=search_text)
            restaurants = result['results']
            form = RestaurantForm()
            context = {'form':form, 'error_message': error_message, 'restaurants': restaurants}
            return render(request, 'restaurants/add.html', context)
        if request.POST['router'] == "2":
            form = RestaurantForm(request.POST)
            if form.is_valid():
                new_restauarant = form.save(commit=False)
                new_restauarant.owner = request.user
                new_restauarant.save()
                return redirect('rest_profile', restaurant_id=new_restauarant.id)
            else:
                error_message = 'Invalid restaurant profile - try again'
        else:
            error_message = 'Invalid restaurant profile - try again'

    form = RestaurantForm()
    context = {'form':form, 'error_message': error_message}
    return render(request, 'restaurants/add.html', context)

# Restaurant Owner Views

def assoc_fac(request, restaurant_id):
    print(request.POST)
    if request.POST['name']:
        facility = Facility(facilityName=request.POST['name'], restaurant_id=restaurant_id, active=True, lat=request.POST['latitude'], lng=request.POST['longitude'])
        facility.save()
        print(facility.id)
        return redirect('rest_profile', restaurant_id=restaurant_id)
    else:
        error_message = 'Invalid restaurant profile - try again'


def rm_fac(request, restaurant_id):
    instance = Facility.objects.get(id=request.POST['facility_id'])
    print(instance)
    instance.delete()
    return redirect('rest_profile', restaurant_id=restaurant_id)


def add_logo(request, restaurant_id):
    logo_file = request.FILES.get('logo-file', None)
    if logo_file:
        s3 = boto3.client('s3')
        key= uuid.uuid4().hex[:6] + logo_file.name[logo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(logo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            logo = Logo(url=url, restaurant_id=restaurant_id)
            logo.save()
        except:
            print('An error has occured uploading your file to S3')
        return redirect('rest_profile', restaurant_id=restaurant_id)
    

class RestUpdate(UpdateView):
    model = Restaurant
    fields = [
        'restaurantName',
        'address',
        'phone',
        'url',
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