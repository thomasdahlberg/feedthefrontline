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
    path('restaurants/<int:rest_id>/assoc_fac/<int:fac_id>/', views.assoc_fac, name='assoc_fac'),
    path('restaurants/<int:rest_id>/rm_fac/<int:fac_id>', views.rm_fac, name='rm_fac'),
    # path('test/', views.test, name="test"),
    path('accounts/signup/', views.signup, name='signup'),
    path('restaurants/<int:restaurant_id>/add_logo/', views.add_logo, name='add_logo'),
]
