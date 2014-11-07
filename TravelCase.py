__author__ = 'Philip'

from google.appengine.ext import db

# database model
class TravelCase(db.Model):
    # traveller
    firstname = db.StringProperty(required=True)
    lastname = db.StringProperty(required=True)
    email = db.EmailProperty(required=True)

    # flight
    airline_symbol = db.StringProperty(required=True)  # e.g. LH
    flight_number = db.IntegerProperty(required=True)  # e.g. 1234
    scheduled_arrival = db.DateTimeProperty(required=True)
    flight_status = db.StringProperty(required=True)  # e.g. 'cancelled'

    # person who is going to pick traveller up
    pickup_firstname = db.StringProperty(required=True)
    pickup_lastname = db.StringProperty(required=True)
    pickup_email = db.EmailProperty(required=True)