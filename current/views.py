# Copyright (c) 2023 Final, All rights reserved.
# Created by Yongji Chen 400168246 for PROCTECH 4IT3.
# SoA Notice: I, Yongji Chen, certify that this material is my original work.
# I certify that no other person's work has been used without due acknowledgement.
# I have also not made my work available to anyone else without their due acknowledgement.

import requests
from django.shortcuts import render
from ipware import get_client_ip
from .models import AirQualityData, LocationData,weatherData
def fetch_weather_data(location):
    api_key = '390d638b54db425d92d23658231304'
    api_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=yes'

    response = requests.get(api_url)
    data = response.json()
    # print(f"Air Quality API URL: {api_url}")
    # print(f"Air Quality API Response: {data}")  # Add this line to print the response content
    location_data = {
        'location': data['location']['name'],
        'region': data['location']['region'],
        'country': data['location']['country'],
        'time_zone': data['location']['tz_id'],
        'local_time': data['location']['localtime'],
        'latitude': data['location']['lat'],
        'longitude': data['location']['lon'],
        'temp_c': data['current']['temp_c'],
        'temp_f': data['current']['temp_f'],
        'humidity': data['current']['humidity'],
        'feelslike_c': data['current']['feelslike_c'],
        'feelslike_f': data['current']['feelslike_f'],

        'wind_speed_kph': data['current']['wind_kph'],
        'wind_speed_mph': data['current']['wind_mph'],
        'wind_direction': data['current']['wind_dir'],
        'wind_degree': data['current']['wind_degree'],

        'expected_precip_mm': data['current']['precip_mm'],
        'expected_precip_in': data['current']['precip_in'],

        'last_updated': data['current']['last_updated'],
        'is_day': data['current']['is_day'],
        'cloud_cover': data['current']['cloud'],
        'condition_text': data['current']['condition']['text'],
        # 'condition_icon': f"https:{data['current']['condition']['icon']}",
        'uv': data['current']['uv'],
        'visibility_km': data['current']['vis_km'],
        'visibility_miles': data['current']['vis_miles'],
        'pressure_mbar': data['current']['pressure_mb'],
        'pressure_in_water': data['current']['pressure_in'],
    }
    # print(location_data)
    # print("Condition Icon URL:", location_data["condition_icon"])
    return location_data
def fetch_air_quality_data(location):
    api_key = '390d638b54db425d92d23658231304'
    api_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=yes'

    response = requests.get(api_url)
    data = response.json()

    air_quality_data = {
        'co': data['current']['air_quality']['co'],
        'no2': data['current']['air_quality']['no2'],
        'o3': data['current']['air_quality']['o3'],
        'so2': data['current']['air_quality']['so2'],
        'pm2_5': data['current']['air_quality']['pm2_5'],
        'pm10': data['current']['air_quality']['pm10'],
        'us_epa_index': data['current']['air_quality']['us-epa-index'],
        'gb_defra_index': data['current']['air_quality']['gb-defra-index'],
    }

    return air_quality_data

def index(request):
    username = request.GET.get('username', 'Guest')

    # Get the client's IP address
    ip_address, _ = get_client_ip(request)
    if ip_address == '127.0.0.1':

        ip_address = '184.145.108.215'  # Use a default IP address if the client's IP cannot be obtained
    else:
        ip_address = ip_address
    # Make an API request to get the location data
    api_key = '314a743429b1e4f1de06e3acea3a6e51'
    api_url = f'http://api.ipstack.com/{ip_address}?access_key={api_key}'
    response = requests.get(api_url)
    location_data = response.json()

    # print(f"IP Address: {ip_address}")  # Debugging
    # print(f"API URL: {api_url}")  # Debugging
    # print(f"Location Data: {location_data}")  # Debugging

    # Fetch weather data (assuming you have already implemented this part)
    weather_data = fetch_weather_data(location_data['city'])


    # Fetch air quality data
    air_quality_data = fetch_air_quality_data(f"{location_data['latitude']},{location_data['longitude']}")
    print('-----------------------')
    print(location_data)
    print('-----------------------')
    print(air_quality_data)
    print('-----------------------')
    print(weather_data)
    location_instance = LocationData(
        ip_address=location_data['ip'],
        ip_type=location_data['type'],
        Continent_Code=location_data['continent_code'],
        Continent_Name = location_data['continent_name'],
        Country_Name = location_data['country_name'],
        Region_Name = location_data['region_name'],
        City = location_data['city'],
        Zip_Code = location_data['zip'],
    )
    location_instance.save()
    weatherData_instance = weatherData(
        location=weather_data['location'],
        region=weather_data['region'],
        country=weather_data['country'],
        time_zone=weather_data['time_zone'],
        local_time=weather_data['local_time'],
        latitude=weather_data['latitude'],
        longitude=weather_data['longitude'],
        TemperatureC=weather_data['temp_c'],
        TemperatureF=weather_data['temp_f'],
        Humidity=weather_data['humidity'],
        Feels_Like_C=weather_data['feelslike_c'],
        Feels_Like_F=weather_data['feelslike_f'],
        Wind_Speed_kph=weather_data['wind_speed_kph'],
        Wind_Speed_Mph=weather_data['wind_speed_mph'],
        Wind_Dirction=weather_data['wind_direction'],
        Wind_Direction_Degree=weather_data['wind_degree'],
        Expected_Precipitation_mm=weather_data['expected_precip_mm'],
        Expected_Precipitation_in=weather_data['expected_precip_in'],
        Last_Updated=weather_data['last_updated'],
        Time_of_Day=weather_data['is_day'],
        Cloud_Cover_Percentage=weather_data['cloud_cover'],
        Weather_Condition=weather_data['condition_text'],
        uv=weather_data['uv'],
        Visibility_KM=weather_data['visibility_km'],
        Visibility_miles=weather_data['visibility_miles'],
        Pressure_milliBar=weather_data['pressure_mbar'],
        Pressure_inWater=weather_data['pressure_in_water'],
    )
    weatherData_instance.save()

    air_quality_instance = AirQualityData(
        Carbon_Monoxide=air_quality_data['co'],
        NO2 = air_quality_data['no2'],
        Ozone = air_quality_data['o3'],
        Sulfur_Dioxide = air_quality_data['so2'],
        Fine_Particulates = air_quality_data['pm2_5'],
        ULTRA_Fine_Particulates = air_quality_data['pm10'],
        USA_EPA_index = air_quality_data['us_epa_index'],
        EU_DAILY_AIR_QUALITY_index = air_quality_data['gb_defra_index'],
    )
    air_quality_instance.save()
    context = {
        'username': username,
        'location_data': location_data,
        'weather_data': weather_data,
        'air_quality_data': air_quality_data,
    }

    return render(request, 'current/index.html', context)
