#!/usr/bin/python2
# -*- coding: utf-8 -*-
from bottle import Bottle, default_app, run, template, view, static_file, route, get, post, request, install, error, abort, redirect, TEMPLATE_PATH
import os
import bottle_mysql
import MySQLdb
from datetime import timedelta
import forecastio
from strings import texts, colors
from random import randint
api_key = "e9a125e0a27d9f347c1c7a3279c28b8f"

def get_weatherdisplay(currently):
    current_texts = texts[currently.icon]
    if current_texts == []:
        return currently.icon
    text = current_texts[randint(0, len(current_texts)-1)]
    bgcolor = colors[currently.icon][0]
    color = colors[currently.icon][1]
    return [text, bgcolor, color]

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@route('/')
def main():
    return template("main")

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='{0}/static'.format(os.getcwd()))

@route("/<latitude>/<longitude>")
def get_weather_from_latlon(latitude, longitude):
    forecast = forecastio.load_forecast(api_key, latitude, longitude)
    info = get_weatherdisplay(forecast.currently())
    if request.is_ajax:
        return {"name":info[0], "bgcolor":info[1], "color":info[2]}
    #return {"name":get_text(forecast.currently().icon), "bgcolor":color[0], "color":color[1]}

TEMPLATE_PATH.insert(0, '{0}/templates'.format(os.getcwd()))

if __name__ == "__main__":
    run(host='localhost', port=8080, reloader=True, debug=True)
else:
    app = default_app()
