#from faker import Factory
#fake = Factory.create('en_US')
from bs4 import BeautifulSoup
import requests


def get_airbnb_img(city='London', page=1):
    url = 'https://www.airbnb.com/s/%s?guests=&checkin=&ss_id=p3ka4v1y&source=bb&page=%s' % (city, page)
    soup = BeautifulSoup(requests.get(url).text)
    links = soup.findAll(itemprop="image")
    r = [link["src"] for link in links]
    print r
    return r


def get_imgs(city='London', count=4):
    r = []
    for i in range(count):
        r += get_airbnb_img(city, i+1)
    return r
