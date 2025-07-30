import folium

map_center = [19.0760, 72.8777]
mymap = folium.Map(location=map_center, zoom_start=10)

folium.Marker(
    [19.8769, 72.8777],
    popup='Mumbai',
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(mymap)

# Para ambientes fora do Jupyter
mymap.save("meu_mapa.html")
