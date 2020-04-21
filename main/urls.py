from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('restaurants/', views.rest_index, name='rest_index'),
    path('restaurants/create/', views.rest_create, name='rest_create'),
    path('restaurants/<int:restaurant_id>', views.rest_profile, name='rest_profile'),
    path('restaurants/<int:pk>/update', views.RestUpdate.as_view(), name='rest_update'),
    path('restaurants/<int:pk>/delete', views.RestDelete.as_view(), name='rest_delete'),
    path('restaurants/<int:restaurant_id>/assoc_fac/', views.assoc_fac, name='assoc_fac'),
    path('restaurants/<int:restaurant_id>/rm_fac/', views.rm_fac, name='rm_fac'),
    path('restaurants/<int:restaurant_id>/rm_logo/', views.rm_logo, name='rm_logo'),
    path('thankyou/', views.thankyou, name="thankyou"),
    path('accounts/signup/', views.signup, name='signup'),
    path('restaurants/<int:restaurant_id>/add_logo/', views.add_logo, name='add_logo'),
    path('restaurants/<int:restaurant_id>/add_merchid/', views.add_merchid, name='add_merchid'),
    path('restaurants/<int:restaurant_id>/rm_merchid/', views.rm_merchid, name='rm_merchid'),
    path('restaurants/<int:restaurant_id>/add_meals/', views.add_meals, name="add_meals"),
    path('restaurants/<int:restaurant_id>/create_transaction/', views.create_transaction, name='create_transaction')
]
