import requests, json
url = 'http://www.trulia.com/_ajax/Geo/SchoolGeoJSON/schoolPoints/?bounds=30.090778328290885%2C-95.89486831054688%2C29.48054810002659%2C-94.91983168945313&v=H34_21&limit=100'
r = requests.get(url)
f = json.loads(r.text.split('\n')[0])['features']

from models.model_airbb import *
init_db()
for i in f:
    s = School()
    s.data = i
    s.city_id = 6
    s.lat = i['geometry']['geometries'][0]['coordinates'][1]
    s.lng = i['geometry']['geometries'][0]['coordinates'][0]
    flush(s)
