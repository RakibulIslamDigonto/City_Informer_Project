from datetime import datetime
from urllib import response
from django.shortcuts import render
from django.views.generic import TemplateView
import requests
from .forms import WeatherForm


# Create your views here.
class WeatherView(TemplateView):
    template_name = 'weatherApp/weather.html'
    form=WeatherForm

    def get(self, request):
        context={
            'form':self.form
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = self.form(request.POST)

        if form.is_valid():
            city = form.cleaned_data['city']
            appid='f54accc5476dfda8ffb023e84391a2fe'
            URL = 'http://api.openweathermap.org/data/2.5/weather'
            PARAMS = {'q':city,'appid':appid, 'units':'metric' }
            
            resp = requests.get(url=URL, params=PARAMS)
            converted_json = resp.json()
            if converted_json['cod']==200:
                weather_info = converted_json['weather'][0]['description']
                icon = converted_json['weather'][0]['icon']
                temperature = converted_json['main']['temp']
                day = datetime.date(datetime.now())

                context={
                    'weather_info':weather_info, 
                    'icon':icon, 
                    'temperature':temperature, 
                    'day':day, 'city':city,
                    'form':form,
                    }
            else:
                msg=converted_json['message']
                context={
                    'msg':msg,
                    'form':form
                }
        return render(request, self.template_name,context)


