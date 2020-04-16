from django.contrib import admin
from .models import Restaurant, Facility, Logo, Transaction, Profile

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Facility)
admin.site.register(Logo)
admin.site.register(Transaction)
admin.site.register(Profile)