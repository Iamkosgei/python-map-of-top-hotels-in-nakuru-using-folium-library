import pandas
import folium

map = folium.Map(location=[-0.2852, 36.0696], zoom_start = 15)

data = pandas.read_csv("hotels_nakuru.txt",sep='\s*,\s*', engine='python')

fg=folium.FeatureGroup(name="Hotel maps")

for x in range(len(data["names"])):
    fg.add_child(folium.Marker(location=[list(data["latitude"])[x],list(data["longitude"])[x]], popup=list(data["names"])[x], icon =folium.Icon(color="green")))

    map.add_child(fg)

map.save("map.html")
