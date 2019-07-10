from folium import Map, DivIcon, Marker
from folium.plugins import HeatMap
import pandas as pd
import numpy as np
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
                  "Nantes", "Madrid", "Rome", "Naples", "London", "Amsterdam", "Warsaw"]


date_today = datetime.today()
date_today_str = date_today.strftime("%Y%m%d")

data = defaultdict(list)
marker = list()
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
    icon = DivIcon(html=f'{tmp["main"]["temp"]}')
    # marker.append(Marker([tmp["coord"]["lat"], tmp["coord"]["lon"]]))

# setup basemap
basemap = Map(location=[data["lat"][0], data["lon"][0]],
              control_scale=True, zoom_start=6,
              tiles="Stamen Toner")

# for m in marker: m.add_to(basemap)

# create dataframe
df = pd.DataFrame(data)
print(df[["lat", "lon", "temp"]])
print(df[["lat", "lon", "temp"]].groupby(["lat", "lon"]))
print(df[["lat", "lon", "temp"]].groupby(["lat", "lon"]).sum())
# maplist = (df[["lat", "lon", "temp"]].groupby(["lat", "lon"]).sum().reset_index().values.tolist())
maplist = (df[["lat", "lon", "temp"]].groupby(["lat", "lon"]).min().reset_index().values.tolist())
# maplist = (df[["lat", "lon", "temp"]].groupby(["lat", "lon"]).min().reset_index().values.tolist())
print(maplist)

cgradient = {np.min(df["temp"]): "blue",
             np.mean(df["temp"]): "lime",
             np.max(df["temp"]): "red"}
cgradient = None

HeatMap(data=maplist, radius=8, max_zoom=1,
        min_val=np.min(df["temp"]),
        max_val=np.max(df["temp"]),
        min_opacity=.1,
        gradient=cgradient,
        blur=15).add_to(basemap)
basemap.save("heatmap_temperatures.html")

print(df.sort_values(by="temp", ascending=False).head())

# we could also to our own visualisation here
def to_rgb(x):
    # norm = (((x - np.min(x)) / (np.max(x) + np.min(x))))
    norm = x / np.max(x)
    return norm

df["norm"] = to_rgb(df["temp"].values)

plt.figure()
for x, y, z, c in df[["lat", "lon", "temp", "norm"]].values:
    # plt.plot(x, y, markersize=z, alpha=0.5, marker="o")
    plt.scatter(x, y, s=c*100, c=str(c),
                vmin=np.min(df["norm"]),
                vmax=np.max(df["norm"]),
                alpha=0.9, marker="o", cmap="thermal")
    print("Color", c)
    plt.text(x, y, f"{z:.2f}")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.colorbar()
plt.savefig("bubble_plot_temperatures.png")


