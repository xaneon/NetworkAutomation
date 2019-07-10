from folium import Map
import matplotlib as mpl
import matplotlib.pyplot as plt
import requests

with open("openweatherapi.key") as fid:
    key = fid.readline()

location = "Frankfurt"
mode = "xml"
units = "metric"
print(key)

baseurl = "https://api.openweathermap.org/data/2.5/"
url_json = f"{baseurl}weather?q={location}&units={units}&APPID={key}"
# url_xml = f"{baseurl}weather?q={location}&{mode}&APPID={key}"

print(url_json)
r = requests.get(url_json)
# r = requests.get(url_xml)
print(r.text)
data = r.json()
# m = Map(location=[45.5236, -122.6750])
# m = Map(location=[data["coord"]["lon"], data["coord"]["lat"]])
m = Map(location=[data["coord"]["lat"], data["coord"]["lon"]])
m.save("example_map.html")
