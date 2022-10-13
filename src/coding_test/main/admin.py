from django.contrib import admin
from main import models

#For Weather model class
class WeatherAdmin(admin.ModelAdmin):
    list_display = ("station", "date", "max_temp","min_temp","ppt")

admin.site.register(models.Weather, WeatherAdmin)

#For Average Weather model class
class AVGWeatherAdmin(admin.ModelAdmin):
    list_display = ("station", "date", "avg_max_temp","avg_min_temp","total_ppt")

admin.site.register(models.AVGWeather, AVGWeatherAdmin)

#For Yield model class
class YieldAdmin(admin.ModelAdmin):
    list_display = ("year","yield_value")

admin.site.register(models.Yield, YieldAdmin)