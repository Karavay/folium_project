import folium
from folium.plugins import MarkerCluster
import pandas as pd

def color_change(elev):
    if elev < 1000:
        return 'green'
    elif elev >= 100 and elev <3000:
        return 'orange'
    else:
        return 'red'

myMap = folium.Map(location=[36.2037068,-113.7666616],tiles = 'CartoDB positron',zoom_start = 5)#width = 500,height = 500,

marker_cluster = MarkerCluster().add_to(myMap)

map_dots = {
    'Руины усадьбы \'Обрина\'':[53.5494456,26.3323365],
    'Moskow':[55.7390099,37.5177689]
}

for key,value in map_dots.items():
    folium.Marker(location=value,popup = key,icon = folium.Icon(color = 'orange')).add_to(marker_cluster)

#add extra points
data = pd.read_csv('Volcanoes_USA.txt')
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']

for lat,lon,elevation in zip(lat,lon,elevation):
    # folium.Marker(location = [lat,lon],popup = str(elevation) + " m",icon = folium.Icon(color = color_change(elevation))).add_to(myMap)
    folium.CircleMarker(location = [lat,lon],radius = 8,popup = str(elevation) + " m",fill_color = color_change(elevation),fill_opacity = 0.8,color = 'gray').add_to(marker_cluster)

myMap.save("myMap1.html")
