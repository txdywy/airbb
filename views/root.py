# -*- coding: utf-8 -*-
from views import *
from flask import (Blueprint, current_app, request, g, url_for, make_response,
                   render_template, redirect, jsonify)
from models.model_test import TestUser, flush
from wsgi import app
from misc import qiniu_agent
import simplejson as json


@app.route('/style')
def style():
    return render_template('test/style.html')


@app.route('/creative')
def creative():
    return render_template('test/creative.html')


@app.route('/gray')
def gray():
    return render_template('test/gray.html')


@app.route('/qn')
def qn():
    return render_template('test/qn.html')


@app.route('/uptoken')
def uptoken():
    d = {'uptoken': qiniu_agent.get_qn_token()}
    return json.dumps(d)


@app.route('/map_test')
def map_test():
    return render_template('test/map.html')


@app.route('/map_<name>')
def map_name(name):
	return render_template('test/map_%s.html' % name)


@app.route('/m')
def m():
    lat, lng = '29.7604267', '-95.3698028'
    return render_template('test/m.html', lat=lat, lng=lng)


@app.route('/')
def index():
    return render_template('index.html')


CITY_LOCATION = {'la': {'lat': '34.052235', 'lng': '-118.243683'},
                 'hu': {'lat': '29.7604267', 'lng': '-95.3698028'},
                 'pa': {'lat': '48.858093', 'lng': '2.294694'},
                 'lo': {'lat': '51.508530', 'lng': '-0.076132'},
                 'va': {'lat': '49.246292', 'lng': '-123.116226'},
                 'ba': {'lat': '41.390205', 'lng': '2.154007'},
                 'sy': {'lat': '-33.865143', 'lng': '151.209900'},
                 }
LA_HOUSES = [
        ['Wine Riot', 34.1839292, -118.3375242, 4, 'http://image1.rent.com/imgr/b0c1da9100b23397411084effcf7669b/200-200'],
        ['New World Mac', 34.057486, -118.2374418, 5, 'http://image1.rent.com/imgr/6a74d975eb14c273f8afde040c8a8d32/200-200'],
        ['LA iPhone Repair', 34.1067475, -117.8571622, 3, 'http://image.rent.com/imgr/823978834bdbacd0aecc02c65b2663f4/200-200'],
        ['Shakespeare Bridge', 34.0833848, -118.3468681, 2, 'http://image.rent.com/imgr/a84c1155e3d1b4a9224559202b898b86/200-200'],
        ['Excalibur Movers', 34.1054515, -118.2785795, 1, 'http://image.rent.com/imgr/5781c6c6c99571f8f3ad6d0ceee38b3b/200-200']
      ]

@app.route('/map')
def map():
    k = request.args.get('k')
    city = CITY_LOCATION.get(k)
    lat, lng = (city['lat'], city['lng']) if city else (CITY_LOCATION['la']['lat'], CITY_LOCATION['la']['lng'])
    if not k or k == 'la':
        houses = LA_HOUSES
    else:
        houses = "[]"
    print '========', houses
    return render_template('map.html', lat=lat, lng=lng, houses=houses)










