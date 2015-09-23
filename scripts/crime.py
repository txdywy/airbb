import requests, json
url = 'http://tiles.trulia.com/crimes/?callback=jQuery1113018686826713383198_1442978794131&geohashes=9vk1%2C9vk4%2C9vk0%2C9v7c%2C9vk3%2C9v7f%2C9v7b%2C9vk6%2C9vk2&v=H34_21&countyCap=500&limit=500&_=1442978794133'
r = requests.get(url)
f = json.loads(r.text[r.text.find('(') + 1: -2])['features']

from models.model_airbb import *
init_db()
for i in f:
    s = Crime()
    s.data = i
    s.city_id = 6
    s.lat = i['geometry']['coordinates'][1]
    s.lng = i['geometry']['coordinates'][0]
    flush(s)
