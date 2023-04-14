CREATE DATABASE IF NOT EXISTS finalexam;

use finalexam;

CREATE TABLE UserInformation (
    ip_address VARCHAR(255),
    ip_Type VARCHAR(255),
    Continent_Code VARCHAR(255),
    Continent_Name VARCHAR(255),
    Country_Name VARCHAR(255),
    Region_Name VARCHAR(255),
    City  VARCHAR(255),
    Zip_Code VARCHAR(255)
);
CREATE TABLE WeatherData (
    Location VARCHAR(255),
    Region VARCHAR(255),
    Country VARCHAR(255),
    Time_Zone VARCHAR(255),
    Local_Time VARCHAR(255),
    Latitude VARCHAR(255),
    Longitude VARCHAR(255),
    TemperatureC VARCHAR(255),
    TemperatureF VARCHAR(255),
    Humidity VARCHAR(255),
    Feels_Like_C VARCHAR(255),
    Feels_Like_F VARCHAR(255),
    Wind_Speed_kph VARCHAR(255),
    Wind_Speed_Mph VARCHAR(255),
    Wind_Dirction VARCHAR(255),
    Wind_Direction_Degree VARCHAR(255),
    Expected_Precipitation_mm VARCHAR(255),
    Expected_Precipitation_in VARCHAR(255),
    Last_Updated VARCHAR(255),
    Time_of_Day VARCHAR(255),
    Cloud_Cover_Percentage VARCHAR(255),
    Weather_Condition VARCHAR(255),
    UV VARCHAR(255),
    Visibility_KM VARCHAR(255),
    Visibility_miles VARCHAR(255),
    Pressure_milliBar VARCHAR(255),
    Pressure_inWater VARCHAR(255)

);
CREATE TABLE AirQuality (
    Carbon_Monoxide VARCHAR(255),
    NO2 VARCHAR(255),
    Ozone VARCHAR(255),
    Sulfur_Dioxide VARCHAR(255),
    Fine_Particulates VARCHAR(255),
    ULTRA_Fine_Particulates VARCHAR(255),
    USA_EPA_index VARCHAR(255),
    EU_DAILY_AIR_QUALITY_index VARCHAR(255)
);

