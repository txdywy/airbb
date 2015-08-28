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
@app.route('/map')
def map():
    k = request.args.get('k')
    city = CITY_LOCATION.get(k)
    lat, lng = (city['lat'], city['lng']) if city else (CITY_LOCATION['la']['lat'], CITY_LOCATION['la']['lng'])
    return render_template('map.html', lat=lat, lng=lng)










