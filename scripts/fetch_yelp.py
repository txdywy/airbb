from misc import yelp
from models.model_airbb import *
def fetch(key='restaurant', location='houston, tx', cls=Restaurant):
    a = yelp.search(key, location)
    x = a['businesses']
    for r in x:
        i=cls()
        i.city_id=6
        i.lat=str(r['location']['coordinate']['latitude'])
        i.lng=str(r['location']['coordinate']['longitude'])
        i.data=r
        flush(i)
