from django.urls import path
from .views import *
urlpatterns = [
    path('weather/',weather, name='weather'),
    path('weather/stats/',weather_stats, name="weather_stats"),
    path('yield/',get_yield,name="get_yield"),
]
