from folium import Map
from folium.plugins import HeatMap
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from collections import defaultdict
import time
from pprint import pprint
from datetime import datetime
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

# now let up build a pandas DataFrame with cities, dates, coordinates and temperatures
list_of_cities = ["Dietzenbach", "Rödermark", "Rodgau", "Frankfurt", "Wiesbaden", "Mainz",
                  "Hamburg", "München", "Kassel", "Osnabrück", "Bielefeld",
                  "Paris", "Strasbourg", "Stuttgart", "Koblenz", "Düsseldorf",
                  "Leipzig", "Berlin", "Jena", "Saarbrücken", "Bonn", "Münster",
                  "Bremen", "Mannheim", "Darmstadt", "Dieburg", "Rennes", "Lille", "Lyon",
                  "Monaco", "Marseille", "Wien", "Potsdam", "Cottbus", "Budapest",
                  "Nantes"]

date_today = datetime.today()
date_today_str = date_today.strftime("%Y%m%d")

data = defaultdict(list)
for city in list_of_cities:
    curr_url = f"{baseurl}weather?q={city}&units={units}&APPID={key}"
    data["cities"].append(city)
    data["dates"].append(datetime.today())
    tmp = requests.get(curr_url).json()
    data["data"].append(tmp)
    data["lon"].append(tmp["coord"]["lon"])
    data["lat"].append(tmp["coord"]["lat"])
    data["temp"].append(tmp["main"]["temp"]) # temperature
    time.sleep(1) # wait 1 sec for API requirements

# setup basemap
basemap = Map(location=[data["lat"][0], data["lon"][0]],
              control_scale=True, zoom_start=6)

# create dataframe
df = pd.DataFrame(data)
print(df[["lat", "lon", "temp"]])
print(df[["lat", "lon", "temp"]].groupby(["lat", "lon"]))
print(df[["lat", "lon", "temp"]].groupby(["lat", "lon"]).sum())
maplist = (df[["lat", "lon", "temp"]].groupby(["lat", "lon"]).sum().reset_index().values.tolist())
print(maplist)

HeatMap(data=maplist, radius=8, max_zoom=6).add_to(basemap)
basemap.save("heatmap_temperatures.html")


