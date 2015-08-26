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
       ]   
for pkg in pkgs:
    local(SUDO_PIP_INSTALL % pkg)
