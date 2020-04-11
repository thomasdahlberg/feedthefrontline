from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Restaurant, Transaction, Facility

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Restuarant Views (Visitor Visible)

def rest_index(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/index.html', { 'restaurants' : restaurants })

def rest_profile(request, rest_id):
    restaurant = Restaurant.objects.get(id=rest_id)
    return render(request, 'restaurants/detail.html', { 'restuarant': restaurant })

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
