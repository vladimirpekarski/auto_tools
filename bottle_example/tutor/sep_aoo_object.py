# -*- coding: utf-8 -*-

from bottle import Bottle, run

app = Bottle()

@app.route('/hello')
def hello():
    return 'Hello world'

run(app, host='localhost', port=8080)