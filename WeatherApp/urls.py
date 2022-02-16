from django.urls import path
from .views import WeatherView


app_name = 'WeatherApp'

urlpatterns = [
    path('', WeatherView.as_view(), name='weather-view')
]
