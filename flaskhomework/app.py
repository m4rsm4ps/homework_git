from flask import Flask, render_template, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    #
    return


@app.route('/requrements/')
def reqs():
    #
    return


@app.route('/generate-users/')
def gen_usr():
    #
    return


@app.route('/mean/')
def averages():
    #
    return


@app.route('/space/')
def astros():
    #
    return


