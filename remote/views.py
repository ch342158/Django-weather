# Copyright (c) 2023 Final, All rights reserved.
# Created by Yongji Chen 400168246 for PROCTECH 4IT3.
# SoA Notice: I, Yongji Chen, certify that this material is my original work.
# I certify that no other person's work has been used without due acknowledgement.
# I have also not made my work available to anyone else without their due acknowledgement.

import requests
from django.shortcuts import render
from ipware import get_client_ip
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
    # ip_address, _ = get_client_ip(request)
    # if not ip_address:
    ip_address, _ = get_client_ip(request)
    if ip_address == '127.0.0.1':

        ip_address = '184.145.108.215'  # Use a default IP address if the client's IP cannot be obtained
    else:
        ip_address = ip_address
    city = request.GET.get('city', None)
    if city:
        try:
            weather_data = fetch_weather_data(city)
            api_key = '314a743429b1e4f1de06e3acea3a6e51'
            api_url = f'http://api.ipstack.com/{ip_address}?access_key={api_key}'
            response = requests.get(api_url)
            location_data = response.json()
        except Exception:
            error_message = "City not found. Displaying current location."
            city = None
            api_key = '314a743429b1e4f1de06e3acea3a6e51'
            api_url = f'http://api.ipstack.com/{ip_address}?access_key={api_key}'
            response = requests.get(api_url)
            location_data = response.json()
            weather_data = fetch_weather_data(location_data['city'])

        air_quality_data = fetch_air_quality_data(f"{location_data['latitude']},{location_data['longitude']}")

        try:
            context = {
            'username': username,
            'location_data': location_data,
            'weather_data': weather_data,
            'air_quality_data': air_quality_data,
            'error_message': error_message,

            }
        except:
            context = {
                'username': username,
                'location_data': location_data,
                'weather_data': weather_data,
                'air_quality_data': air_quality_data,
            }

        return render(request, 'remote/index.html', context)

    else:
        error_message = "City not found. Displaying current location."
        city = None
        api_key = '314a743429b1e4f1de06e3acea3a6e51'
        api_url = f'http://api.ipstack.com/{ip_address}?access_key={api_key}'
        response = requests.get(api_url)
        location_data = response.json()
        weather_data = fetch_weather_data(location_data['city'])


    air_quality_data = fetch_air_quality_data(f"{location_data['latitude']},{location_data['longitude']}")

    context = {
        'username': username,
        'location_data': location_data,
        'weather_data': weather_data,
        'air_quality_data': air_quality_data,
        'error_message': error_message,

    }


    return render(request, 'remote/index.html', context)
