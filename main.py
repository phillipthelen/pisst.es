#!/usr/bin/python2
# -*- coding: utf-8 -*-
from bottle import Bottle, default_app, run, template, view, static_file, route, get, post, request, install, error, abort, redirect, TEMPLATE_PATH
import os
import bottle_mysql
import MySQLdb
from datetime import timedelta

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@route('/')
def main():
    return template("main")

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='{0}/static'.format(os.getcwd()))

TEMPLATE_PATH.insert(0, '{0}/templates'.format(os.getcwd()))

if __name__ == "__main__":
    run(host='localhost', port=8080, reloader=True, debug=True)
else:
    app = default_app()
