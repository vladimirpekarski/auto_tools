# -*- coding: utf-8 -*-

from bottle import route, run, template


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>', name=name)

run(host='localhost', post=8080, debug=True)