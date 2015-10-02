# -*- coding: utf-8 -*-
from fabric.api import *
SUDO_PIP_INSTALL = 'sudo pip install %s'
pkgs = ['flask',               #flask web framework
        'sqlalchemy',          #orm
        'Flask-SQLAlchemy',    #flask plugin for sqlalchemy
        'supervisor',          #uwsgi process manager
        'uwsgi',               #uwsgi container
        'Flask-Babel',         #i18n
        'simplejson',          #better json
        'qiniu',                #qiniu sdk
        'leancloud-sdk',
        'oauth2',
       ]   
for pkg in pkgs:
    local(SUDO_PIP_INSTALL % pkg)
