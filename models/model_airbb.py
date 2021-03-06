# -*- coding: utf-8 -*-
from models import *

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    lat = Column(String(50))
    lng = Column(String(50))
    name = Column(String(128))
    country = Column(String(128))
    abbr = Column(String(8), index=True)
    info = Column(String(512))
    img = Column(String(512))
    url = Column(String(512))

    def __repr__(self):
        return '<City %r>' % (self.id)


class Area(Base):
    __tablename__ = 'area'
    id = Column(Integer, primary_key=True)
    lat = Column(String(50))
    lng = Column(String(50))
    city_id = Column(Integer, index=True)
    name = Column(String(128))
    info = Column(String(512))
    img = Column(String(512))
    url = Column(String(512))


    def __repr__(self):
        return '<Area %r>' % (self.id)


class HouseOld(Base):
    __tablename__ = 'house_old'
    id = Column(Integer, primary_key=True)
    lat = Column(String(50))
    lng = Column(String(50))
    city_id = Column(Integer, index=True)
    title = Column(String(128))
    info = Column(String(512))
    zipcode = Column(String(16))
    address = Column(String(512))
    img = Column(String(512))
    url = Column(String(512))


    def __repr__(self):
        return '<House_old %r>' % (self.id)


class House(Base):
    __tablename__ = 'house'
    id = Column(Integer, primary_key=True)
    lat = Column(String(50))
    lng = Column(String(50))
    com_id = Column(Integer, index=True)
    data = Column(MutableDict.as_mutable(PickleType))


    def __repr__(self):
        return '<%r %r>' % (self.__tablename__, self.id)


class Community(Base):
    __tablename__ = 'community'
    id = Column(Integer, primary_key=True)
    lat = Column(String(50))
    lng = Column(String(50))
    city_id = Column(Integer, index=True)
    title = Column(String(128))
    info = Column(Text)
    total_price = Column(String(50))
    square = Column(String(50))
    house_type = Column(String(50))
    zipcode = Column(String(16))
    address = Column(String(512))
    img = Column(String(512))
    url = Column(String(512))
    vir_url = Column(String(512))
    img_bk = Column(String(512))
    sale = Column(Integer, default=0)


    def __repr__(self):
        return '<community %r>' % (self.id)


class School(Base):
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True)
    lat = Column(String(50))
    lng = Column(String(50))
    city_id = Column(Integer, index=True)
    data = Column(MutableDict.as_mutable(PickleType))


    def __repr__(self):
        return '<school %r>' % (self.id)


class Crime(Base):
    __tablename__ = 'crime'
    id = Column(Integer, primary_key=True)
    lat = Column(String(50))
    lng = Column(String(50))
    city_id = Column(Integer, index=True)
    data = Column(MutableDict.as_mutable(PickleType))


    def __repr__(self):
        return '<crime %r>' % (self.id)


class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    lat = Column(String(50))
    lng = Column(String(50))
    city_id = Column(Integer, index=True)
    data = Column(MutableDict.as_mutable(PickleType))

    def __repr__(self):
        return '<restaurant %r>' % (self.id)


class Health(Base):
    __tablename__ = 'health'
    id = Column(Integer, primary_key=True)
    lat = Column(String(50))
    lng = Column(String(50))
    city_id = Column(Integer, index=True)
    data = Column(MutableDict.as_mutable(PickleType))

    def __repr__(self):
        return '<health %r>' % (self.id)


class Park(Base):
    __tablename__ = 'park'
    id = Column(Integer, primary_key=True)
    lat = Column(String(50))
    lng = Column(String(50))
    city_id = Column(Integer, index=True)
    data = Column(MutableDict.as_mutable(PickleType))

    def __repr__(self):
        return '<park %r>' % (self.id)


class Shop(Base):
    __tablename__ = 'shop'
    id = Column(Integer, primary_key=True)
    lat = Column(String(50))
    lng = Column(String(50))
    city_id = Column(Integer, index=True)
    data = Column(MutableDict.as_mutable(PickleType))

    def __repr__(self):
        return '<shop %r>' % (self.id)


class Entertainment(Base):
    __tablename__ = 'entertainment'
    id = Column(Integer, primary_key=True)
    lat = Column(String(50))
    lng = Column(String(50))
    city_id = Column(Integer, index=True)
    data = Column(MutableDict.as_mutable(PickleType))

    def __repr__(self):
        return '<entertainment %r>' % (self.id)


class User(Base):
    __tablename__ = 'user'

    POWER_ADMIN = 2**9

    id = Column(Integer, primary_key=True)
    email = Column(String(128))
    phone = Column(String(32))
    pw_hash = Column(String(128))
    name = Column(String(32))
    power = Column(Integer, default=0)


    def __repr__(self):
        return '<User %r>' % (self.id)
