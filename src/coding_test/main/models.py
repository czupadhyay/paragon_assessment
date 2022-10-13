from django.db import models

class Weather(models.Model):
    station = models.CharField(max_length=15)
    date = models.CharField(max_length=8)
    max_temp = models.IntegerField()
    min_temp = models.IntegerField()
    ppt = models.IntegerField()

    class Meta:
        verbose_name = "Weather"
        unique_together = (("station", "date"),)

    def __str__(self):
        return str(self.station)

class AVGWeather(models.Model):
    station = models.CharField(max_length=15)
    date = models.CharField(max_length=8)
    avg_max_temp = models.IntegerField()
    avg_min_temp = models.IntegerField()
    total_ppt = models.IntegerField()

    class Meta:
        verbose_name = "AVGWeather"

    def __str__(self):
        return str(self.station)

class Yield(models.Model):
    year = models.CharField(max_length=10,unique=True)
    yield_value = models.IntegerField()
    
    class Meta:
        verbose_name = "Yield"

    def __str__(self):
        return str(self.year)

