from django.test import TestCase
from django.test.client import RequestFactory
from django.test import TestCase
from main.models import Weather
from .views import *

class AppTestCase(TestCase):
    @classmethod
    def setUp(self):
        Weather.objects.create(station="USC001107",date="1985010",max_temp=20,min_temp=19,ppt=12)
        AVGWeather.objects.create(station="USC00111280",date="20051005",avg_max_temp=20,avg_min_temp=19,total_ppt=12)
        Yield.objects.create(year="2011",yield_value=12)
        self.factory=RequestFactory()

    def test_weather_search_data(self):
        req=self.factory.get("/api/weather/?date=1985010&&station=USC001107")
        response=weather(req)
        self.assertEqual(response.data['weather_objs'][0].get("date"),"1985010")
        # self.assertEqual(data.date,"1985010")

    def test_get_yield_data(self):
        req=self.factory.get("/api/yield")
        response=get_yield(req)
        self.assertEqual(response.data['status'],200)
        self.assertEqual(response.data['yield'][0].get('yield_value'),12)
    
    def test_avg_weather(self):
        req=self.factory.get("/api/weather/stats/?date=20051005&station=USC00111280")
        response=weather_stats(req)
        self.assertEqual(response.data['weather_stats'][0].get("date"),"20051005")