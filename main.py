__author__ = 'Philip'

# imports
import sys
import os.path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
from flask import Flask, request, render_template

import datetime
from TravelCase import TravelCase
import AskLufthansa

# create a Flask app. This is the actual webapp handler.
app = Flask(__name__)
app.config['DEBUG'] = True

# note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


# index page, built based on the template 'index_old.html
@app.route('/')
def index():
    form_url = "/hello2"  # target url to which this page POSTs form data to
    return render_template('index_old.html', **locals())  # render page


# simple, silly version of feedback page
# target page that just returns the data entered on the index page
@app.route('/hello',
           methods=['POST', 'GET'])  # note: page supports POST and GET
def hello():
    output = "nothing"

    if 'myName' in request.form:  # check if there actually is form data
        output = ""

        # iterate over variables passed in the form
        for key, value in request.form.items():
            output += str(key) + ': ' + str(value) + '<br>'  # append key-value

    return 'Yeah man, you entered: <br><br>' + output  # return dumb HTML


# more sophisticated version of a feedback page
# target page, this time built dynamically from a template
@app.route('/hello2', methods=['POST'])  # note: this page only supports POST!
def hello2():
    # check input data
    passed_vars = dict()  # save the variables posted to this page here
    if 'firstname' in request.form:  # check if vars contain key
        for key, value in request.form.items():  # iterate over key-value pairs
            passed_vars[key] = value  # add key-value pair to dict
        passed_vars.pop('submit')

        # TODO: verify flight number
        flight_date = datetime.datetime(
            int(passed_vars['flight_year']),
            int(passed_vars['flight_month']),
            int(passed_vars['flight_day']))

        flight_status = AskLufthansa.get_flight_status(
            passed_vars['airline_symbol'],
            passed_vars['flight_number'],
            flight_date)

        if flight_status == "incorrect":
            # TODO: exception handling!
            return 'Wrong flight information!'

        # TODO: verify email addresses

        # generate DB entry
        travel_case = TravelCase(
            firstname=passed_vars['firstname'],
            lastname=passed_vars['lastname'],
            email=passed_vars['email'],
            airline_symbol=passed_vars['airline_symbol'],
            flight_number=int(passed_vars['flight_number']),  # TODO
            scheduled_arrival=flight_date,

            flight_status=flight_status,
            pickup_firstname=passed_vars['pickup_firstname'],
            pickup_lastname=passed_vars['pickup_lastname'],
            pickup_email=passed_vars['pickup_email'])

        travel_case.put()
        pickup_id = travel_case.key()

        # return success page
        return render_template('welcome_old.html', **locals())

    # if, for some reason, the form data is nonsense
    return 'Sorry, no reasonable form data posted.'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

