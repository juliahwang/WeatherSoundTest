from django.db import models


# Create your models here.


class Weather(models.Model):
    # latitude = models.FloatField(verbose_name='위도')
    # longitude = models.FloatField(verbose_name='경도')
    # location = models.CharField(max_length=100)
    time_range = models.DateTimeField(auto_created=True)
    name_area = models.CharField(max_length=100)
    weather = models.CharField(max_length=100)

    def __str__(self):
        return "{}'s weather is {} at {}".format(
            self.name_area, self.weather, self.time_range
        )


import requests


class GetWeather:
    def __init__(self, secret_key_weather, secret_key_google_geo, ):
        self.secret_key_weather = secret_key_weather
        self.secret_key_google_geo = secret_key_google_geo
        self.weather = dict()

    def get_geometry(self, *location):
        url = "https://maps.googleapis.com/maps/api/geocode/json" \
              "?latlng={LATITUDE},{LONGITUDE}" \
              "&key={SECRET_KEY}" \
              "&language=ko" \
              "&result_type={result_type}".format(LATITUDE=location[0],
                                                  LONGITUDE=location[1],
                                                  SECRET_KEY=self.secret_key_google_geo,
                                                  result_type="sublocality", )
        address = requests.get(url).json()["results"][2]["formatted_address"]
        return address

    def get_weather_info(self, *location):
        url = "https://api.darksky.net/forecast/" \
              "{SECRET_KEY}/" \
              "{LATITUDE},{LONGITUDE}".format(
            SECRET_KEY=self.secret_key_weather,
            LATITUDE=location[0],
            LONGITUDE=location[1], )
        data = requests.get(url).json()
        addr = self.get_geometry(*location)

        if not addr in self.weather or \
                        (data["currently"]["time"].hour - self.weather[addr]["time"].hour) >= 1:
            self.weather[addr] = {
                "time": data["hourly"]["data"][0]["time"],  # timeRange
                "icon": data["currently"]["icon"],  # weather
                "location_name": addr,
            }

    def get_info(self, *location):
        self.get_weather_info(*location)
        return self.weather
