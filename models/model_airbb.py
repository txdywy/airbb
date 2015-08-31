# -*- coding: utf-8 -*-
from models import *
class House(Base):
    __tablename__ = 'house'
    id = Column(Integer, primary_key=True)
    lat = Column(String(50))
    lng = Column(String(50))
    tag = Column(String(50), index=True)
    city = Column(String(50))
    country = Column(String(50))
    info = Column(String(512))
    address = Column(String(512))
    img = Column(String(512))
    url = Column(String(512))

    
    def __repr__(self):
        return '<House %r>' % (self.id)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(128))
    phone = Column(String(32))
    pw_hash = Column(String(128))
    name = Column(String(32))


    def __repr__(self):
        return '<User %r>' % (self.id)