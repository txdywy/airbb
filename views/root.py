# -*- coding: utf-8 -*-
from views import *
from flask import (Blueprint, current_app, request, g, url_for, make_response,
                   render_template, redirect, jsonify, flash, session)
from models.model_airbb import *
from werkzeug import check_password_hash, generate_password_hash
from wsgi import app
from misc import qiniu_agent
import simplejson as json
import functools


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])


def login_required(f):
    @functools.wraps(f)
    def func(*args, **kwargs):
        if 'user_id' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return func


def power_required(power=User.POWER_ADMIN):
    def deco(f):
        @functools.wraps(f)
        def func(*args, **kwargs):
            if g.user.power & power:
                return f(*args, **kwargs)
            else:
                return redirect(url_for('login'))
        return func
    return deco


def exr(f):
    @functools.wraps(f)
    def func(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception, e:
            return str(e)
    return func


@app.route('/register', methods=['GET', 'POST'])
@exr
def register():
    """Registers the user."""
    if g.user:
        return redirect(url_for('index'))
    error = None
    if request.method == 'POST':
        email = request.form['email'].strip()
        if not email or '@' not in email:
            error = 'email无效'
        elif not request.form['password']:
            error = '需要输入密码'
        elif request.form['password'] != request.form['password2']:
            error = '密码错误'
        elif User.query.filter_by(email=email).first():
            error = 'email已被使用'
        else:
            u = User(email=email, pw_hash=generate_password_hash(request.form['password']))
            flush(u)
            session['user_id'] = u.id
            flash('注册成功')
            return redirect(url_for('index'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Logs the user in."""
    if g.user:
        return redirect(url_for('index'))
    error = None
    if request.method == 'POST':
        try:
            email = request.form['email']
        except:
            abort(404)
        user = User.query.filter_by(email=email).first()
        if user is None:
            error = '用户名/密码无效'
        elif not check_password_hash(user.pw_hash, request.form['password']):
            error = '用户名/密码无效'
        else:
            flash('登录成功')
            session['user_id'] = user.id
            return redirect(url_for('index'))
    if error:
        flash(error)
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    """Logs the user out."""
    flash('注销成功')
    session.pop('user_id', None)
    return redirect(url_for('index'))


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

@app.route('/car')
def car():
    return render_template('test/carousel.html')


@app.route('/area')
def area():
    k = request.args.get('k')
    city = City.query.filter_by(abbr=k).first()
    if not city:
        city = City.query.get(4)
    cid = city.id
    areas = Area.query.filter_by(city_id=cid).all()
    city = City.query.get(cid)
    print '=======',len(areas)
    return render_template('area.html', city=city, areas=areas, num=len(areas))


@app.route('/')
def index():
    city = request.args.get('c')
    city = city if city else u'\u57ce\u5e02'
    return render_template('index.html', city=city)


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
    city = City.query.filter_by(abbr=k).first()
    if not city:
        city = City.query.filter_by(abbr='la').first()
    lat, lng = (city.lat, city.lng) if city else (CITY_LOCATION['la']['lat'], CITY_LOCATION['la']['lng'])
    houses = House.query.filter_by(city_id=city.id).all()
    return render_template('map.html', lat=city.lat, lng=city.lng, houses=houses)


@app.route('/finance')
def finance():
    return render_template('finance.html')


@app.route('/operation')
def operation():
    return render_template('operation.html')


@app.route('/com')
def com():
    k = request.args.get('k')
    city = City.query.filter_by(abbr=k).first()
    if not city:
        city = City.query.filter_by(abbr='hu').first()
    lat, lng = (city.lat, city.lng) if city else (CITY_LOCATION['la']['lat'], CITY_LOCATION['la']['lng'])
    coms = Community.query.filter_by(city_id=city.id).all()
    schs = School.query.filter_by(city_id=city.id).all()
    cris = Crime.query.filter_by(city_id=city.id).all()
    rests = Restaurant.query.filter_by(city_id=city.id).all()
    heas = Health.query.filter_by(city_id=city.id).all()
    parks = Park.query.filter_by(city_id=city.id).all()
    shops = Shop.query.filter_by(city_id=city.id).all()
    ents = Entertainment.query.filter_by(city_id=city.id).all()
    return render_template('com.html', lat=city.lat, lng=city.lng, coms=coms, schs=schs, cris=cris, rests=rests, heas=heas, parks=parks, shops=shops, ents=ents)


@app.route('/info')
def info():
    com_id = request.args.get('c')
    com = Community.query.get(com_id)
    if not com:
        return 'error'
    city = City.query.get(com.city_id)
    if not city:
        city = City.query.filter_by(abbr='hu').first()
    #lat, lng = (city.lat, city.lng) if city else (CITY_LOCATION['la']['lat'], CITY_LOCATION['la']['lng'])
    coms = [com]
    hous = House.query.filter_by(com_id=com_id).all()
    lat, lng = (hous[0].lat, hous[0].lng) if hous else (CITY_LOCATION['la']['lat'], CITY_LOCATION['la']['lng'])
    schs = School.query.filter_by(city_id=city.id).all()
    cris = Crime.query.filter_by(city_id=city.id).all()
    rests = Restaurant.query.filter_by(city_id=city.id).all()
    heas = Health.query.filter_by(city_id=city.id).all()
    parks = Park.query.filter_by(city_id=city.id).all()
    shops = Shop.query.filter_by(city_id=city.id).all()
    ents = Entertainment.query.filter_by(city_id=city.id).all()
    return render_template('info.html', lat=lat, lng=lng, coms=coms, schs=schs, cris=cris, rests=rests, heas=heas, parks=parks, shops=shops, ents=ents, hous=hous)
