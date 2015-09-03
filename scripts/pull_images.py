from models.model_airbb import *
from misc import airbnb

def pull():
    cs = City.query.all()
    for c in cs:
        if c.abbr=='la' or c.id==1:
            pass
        else:
            r = airbnb.get_imgs(city=c.name)
            hs = House.query.filter_by(city_id=c.id).all()
            for h in hs:
                h.img = r[h.id-hs[0].id]
                flush(h)

