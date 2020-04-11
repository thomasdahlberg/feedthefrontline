from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('restaurants/', views.rest_index, name='rest_index'),
    path('restaurants/', views.rest_profile, name='rest_profile'),
    path('restaurants/<int:rest_id>/assoc_fac/<int:fac_id>/', views.assoc_fac, name='assoc_fac'),
    path('restaurants/<int:rest_id>/rm_fac/<int:fac_id>', views.rm_fac, name='rm_fac'),
]
