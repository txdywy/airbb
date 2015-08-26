# -*- coding: utf-8 -*-
from flask import Flask
from models import db_session
from config import DEBUG
from flask.ext.babel import Babel

#init app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_Hans_CN'
babel = Babel(app)

#clean db_session(sqlalchemy, not actual db) for each request
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

#attache view to app
from views import test, root
app.register_blueprint(test.view)
