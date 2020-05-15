import requests
from django.shortcuts import render ,redirect
from .models import City
# Create your views here.
def index(request):
	url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=7b0944ba877c34315d2065fc215ea25b&units=metric'

	
	weather_data=[]

	cities=City.objects.all()

	for city in cities:
		r = requests.get(url.format(city.name)).json()	

		city_weather = {
			'city':city.name,
			'temperature':r['main']['temp'],
			'description':r['weather'][0]['description'],
			'icon':r['weather'][0]['icon']
		} 

		weather_data.append(city_weather)	 
	context={
	'weather_data':weather_data,
	}	   
	return render(request, 'index.html',context)



def AddCity(request):
	url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=7b0944ba877c34315d2065fc215ea25b&units=metric'
	err_msg=''
	message=''
	message_class=''
	if request.method=='POST':
		new_city=request.POST['City']
		r=requests.get(url.format(new_city)).json()
		num_of_times=City.objects.all().filter(name=new_city).count()
		if num_of_times == 0:
			data=City(name=new_city)
			if r['cod'] ==200:
				data.save()
			else:
				err_msg='City Enter is IN-CORRECT Please Enter a Valid City.'
		else:
			err_msg='City already present in the List .'
	if err_msg:
		message=err_msg
		message_class='alert-danger'
	else:
		message='City Added Succesfully in the List.'
		message_class='alert-success'
	
	return redirect('index')


def deleteCity(request ,city_id):
	remove_city=City.objects.all().filter(name=city_id).delete()
	return redirect('index')
