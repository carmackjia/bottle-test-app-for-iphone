import bottle
from bottle import request, run, route, get, post, template

@route("/")
def index():
    return "<p>Hello from my iphone</p>"

run(host="0.0.0.0", port=8000)
