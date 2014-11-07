__author__ = 'Philip'

# imports
import sys
import os.path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
from flask import Flask, request, render_template


# create a Flask app. This is the actual webapp handler.
app = Flask(__name__)
app.config['DEBUG'] = True


# index page
@app.route('/')
def index():
    form_url = "/fbauth"  # target url to which this page POSTs form data to
    return render_template('index.html', **locals())  # render page


@app.route('/fbauth', methods=['POST', 'GET'])
def fbauth():
    return render_template('index.html', **locals())  # render page


@app.route('/enterdate', methods=['POST', 'GET'])
def enterdate():
    form_url = '/wait'
    return render_template('enterdate.html', **locals())


@app.route('/wait', methods=['POST', 'GET'])
def wait():
    return render_template('wait.html', **locals())


@app.route('/results', methods=['POST', 'GET'])
def results():
    passed_vars = dict()
    passed_vars['friend 1'] = 'city 1, 399$'
    passed_vars['friend 2'] = 'city 2, 199$'
    return render_template('results.html', **locals())


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404