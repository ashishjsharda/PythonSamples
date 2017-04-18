'''
Created on Apr 18, 2017

@author: asharda
'''
import geocoder
import json
import requests
freegeoip = "http://freegeoip.net/json"
geo_r = requests.get(freegeoip)
geo_json = geo_r.json()

user_postition = [geo_json["latitude"], geo_json["longitude"], geo_json["city"], geo_json["region_name"]]

print(user_postition)