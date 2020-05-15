from django.urls import path
from . import views


urlpatterns  =  [
	path('',views.index ,name='index'),
	path('AddCity/',views.AddCity ,name='AddCity'),
	path('deleteCity/<city_id>/',views.deleteCity ,name='deleteCity'),
]