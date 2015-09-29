from misc import yelp
from models.model_airbb import *
def fetch_rest(location):
    a = yelp.search('restaurant', location)
    x = a['businesses']
    for r in x:
        i=Restaurant()
        i.city_id=6
        i.lat=str(r['location']['coordinate']['latitude'])
        i.lng=str(r['location']['coordinate']['longitude'])
        i.data=r;flush(i)
