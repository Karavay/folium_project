import folium

myMap = folium.Map(location=[53.5494456,26.3323365],zoom_start = 6)

folium.Marker(location=[53.5494456,26.3323365],popup = 'Руины усадьбы \'Обрина\'',icon = folium.Icon(color = 'orange')).add_to(myMap)






myMap.save("myMap1.html")
