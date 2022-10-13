from rest_framework import serializers
from .models import *


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ["station", "date", "max_temp","min_temp","ppt"]

class AVGWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = AVGWeather
        fields = ["station", "date", "avg_max_temp","avg_min_temp","total_ppt"]

class YieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yield
        fields = ["year","yield_value"]
