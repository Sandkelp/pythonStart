import folium
import pandas as pd
import json

data = pd.read_csv("C:\\Users\\ssubh\\OneDrive\\Desktop\\python\\Basic\\volcano.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_changer(height):
    if height > 1000:
       return 'green'
    elif 1000 <= height < 3000:
        return 'orange' 
    else:
        return 'red'

map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles = "Stamen Terrain")# tells the code to go to one location
fgv = folium.FeatureGroup(name="Volcanos")

for lt,ln,elv, in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln] , radius = 6, popup=str(elv) + "m",# makes a green marker that says hello at the specifyed point
    fill_color = color_changer(elv), color = 'grey',fill_opacity=0.7))

fgp = folium.FeatureGroup(name= "Population")
fgp.add_child(folium.GeoJson(data=open('C:\\Users\\ssubh\\Downloads\\world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 1000000 
else 'orange' if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fgp)
map.add_child(fgv)

map.add_child(folium.LayerControl())

map.save("Map1.html")#saves the map 