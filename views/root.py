# -*- coding: utf-8 -*-
from views import *
from flask import (Blueprint, current_app, request, g, url_for, make_response,
                   render_template, redirect, jsonify)
from models.model_test import TestUser, flush
from wsgi import app
from misc import qiniu_agent
import simplejson as json

@app.route('/')
def index():
    return render_template('test/style.html')


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


@app.route('/map')
def map():
    return render_template('test/map.html')


@app.route('/map_<name>')
def map_name(name):
	return render_template('test/map_%s.html' % name)


@app.route('/m')
def m():
    lat, lng = '29.7604267', '-95.3698028'
    return render_template('test/m.html', lat=lat, lng=lng)