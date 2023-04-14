# Copyright (c) 2023 Final, All rights reserved.
# Created by Yongji Chen 400168246 for PROCTECH 4IT3.
# SoA Notice: I, Yongji Chen, certify that this material is my original work.
# I certify that no other person's work has been used without due acknowledgement.
# I have also not made my work available to anyone else without their due acknowledgement.

from django.db import models
class weatherData(models.Model):
    location = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    time_zone = models.CharField(max_length=100)
    local_time = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    TemperatureC = models.FloatField()
    TemperatureF = models.FloatField()
    Humidity = models.IntegerField()
    Feels_Like_C = models.FloatField()
    Feels_Like_F = models.FloatField()
    Wind_Speed_kph = models.FloatField()
    Wind_Speed_Mph = models.FloatField()
    Wind_Dirction = models.CharField(max_length=10)
    Wind_Direction_Degree = models.IntegerField()
    Expected_Precipitation_mm = models.FloatField()
    Expected_Precipitation_in = models.FloatField()
    Last_Updated = models.DateTimeField()
    Time_of_Day = models.BooleanField()
    Cloud_Cover_Percentage = models.IntegerField()
    Weather_Condition = models.CharField(max_length=100)
    uv = models.FloatField()
    Visibility_KM = models.FloatField()
    Visibility_miles = models.FloatField()
    Pressure_milliBar = models.FloatField()
    Pressure_inWater = models.FloatField()


class AirQualityData(models.Model):
    weather_data = models.OneToOneField(weatherData, on_delete=models.CASCADE, null=True)
    Carbon_Monoxide = models.FloatField()
    NO2 = models.FloatField()
    Ozone = models.FloatField()
    Sulfur_Dioxide = models.FloatField()
    Fine_Particulates = models.FloatField()
    ULTRA_Fine_Particulates = models.FloatField()
    USA_EPA_index = models.IntegerField()
    EU_DAILY_AIR_QUALITY_index = models.IntegerField()

class LocationData(models.Model):
    ip_address = models.GenericIPAddressField()
    ip_type = models.CharField(max_length=10)
    Continent_Code = models.CharField(max_length=100)
    Continent_Name = models.CharField(max_length=100)
    Country_Name = models.CharField(max_length=100)
    Region_Name = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Zip_Code=models.CharField(max_length=100)
