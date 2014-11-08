__author__ = 'Philip'

# imports
import sys
import os.path
import json
import scrapper
import facepy
import fb_calls
from geopy.geocoders import Nominatim
import requests


sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
from flask import Flask, render_template, redirect, url_for, session, \
    request, send_from_directory
from flask_oauth import OAuth

fb_response = json.loads('{"data": [{"name": "Frieder Bluemle","location": {"id": "108212625870265","name": "Mountain View, California"},"id": "548055444"},{"name": "Robin Schmid","location": {"id": "108212625870265","name": "Marseille"},"id": "1275411665"},{"name": "Patrick Schneider","location": {"id": "108212625870265","name": "New York, USA"},"id": "1640723486"},{"name": "Philipp Schreiber","location": {"id": "108212625870265","name": "Rome, Italy"},"id": "1720495860"},{"name": "Frederik Greve","location": {"id": "106203279418033","name": "London"},"id": "100000603993850"},{"name": "Linus Braun","location": {"id": "108212625870265","name": "Madrid"},"id": "779131692123189"},{"name": "Dennis Charles","location": {"id": "108212625870265","name": "Moscow"},"id": "100001685564479"},{"name": "Kaley","location": {"id": "108212625870265","name": "Athens"},"id": "100004069003465"}],"paging": {"next": "https://graph.facebook.com/v2.2/10204134077049823/friends?fields=name,location&limit=25&offset=25&__after_id=enc_AeyOvUtLi65lGbIDAm1Ax01C7JF1LVA_LHmKHY9YHbm0RaGc6EdiDS71Qmu7SdSEjhJHjxcFI58zmbRSjEVDuLFJ"},"summary": {"total_count": 1099}}')

# create a Flask app. This is the actual webapp handler.
app = Flask(__name__)
app.config['DEBUG'] = True


# index page
@app.route('/')
def index():
    form_url = "/facebook_login"  # target url to which this page POSTs form data to

    return render_template('index.html', **locals())  # render page


@app.route('/fbauth', methods=['POST', 'GET'])
def fbauth():
    return render_template('index.html', **locals())  # render page


def getFriendsList():
    return facebook.get('/me/friends').data


@app.route('/enterdate', methods=['POST', 'GET'])
def enterdate():
    form_url = '/wait'
    data = facebook.get('/me').data
    if 'id' in data and 'name' in data:
        user_id = data['id']
        user_name = data['name']
        first_name = data['first_name']
        location = data['location']['name']

    return render_template('enterdate.html', **locals())


def get_iata(lat, lon):
    url = 'https://www.swiss.com/web/api/SwissService.asmx'
    xml_request = '''<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><RequestNearestAirportInformation xmlns="http://www.swiss.com/"><ota_ScreenTextRQ MessageFunction="%s,%s" PrimaryLangID="de" Version="1" xmlns="http://www.opentravel.org/OTA/2003/05"><POS><Source><RequestorID ID="195004ec-da2a-4cba-8db0-f0ad20094802" MessagePassword="61022420B9C8FA46999094D06379D83B"/></Source></POS></ota_ScreenTextRQ></RequestNearestAirportInformation></s:Body></s:Envelope>'''
    headers = {'content-type': 'text/xml'}

    response = requests.post(url, data=xml_request % (lon,lat), headers=headers).content
    return response[response.find("<TextData>CityCode#")+19:response.find("<TextData>CityCode#")+22]



@app.route('/wait', methods=['POST', 'GET'])
def wait():
    friends_list = fb_response
    geolocator = Nominatim()



    for friend in friends_list['data']:
        location = geolocator.geocode(friend['location']['name'])

        print(friend['location']['name'] + str(location.latitude) + " " + str(location.longitude) + " ")


    return render_template('wait.html', **locals())


@app.route('/results', methods=['POST', 'GET'])
def results():
    passed_vars = dict()
    passed_vars['friend 1'] = 'city 1, 399$'
    passed_vars['friend 2'] = 'city 2, 199$'
    return render_template('results.html', **locals())


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'static/images/favicon.ico')

@app.route('/privacy', methods=['GET'])
def privacy():
    return render_template('privacy.html', **locals())

# #######

FACEBOOK_APP_ID = '298338373704084'
FACEBOOK_APP_SECRET = 'dea6ece10b93e36b3c2262b80d338224'

app.secret_key = "\xf3\x00\x833\xa0\xee\xee\xf2Ghi\x81t\xf2\x0f3\xcd\xd2\x15J\x99\x17;\xfb"

oauth = OAuth()

facebook = oauth.remote_app('facebook',
                            base_url='https://graph.facebook.com/',
                            request_token_url=None,
                            access_token_url='/oauth/access_token',
                            authorize_url='https://www.facebook.com/dialog/oauth',
                            consumer_key=FACEBOOK_APP_ID,
                            consumer_secret=FACEBOOK_APP_SECRET,
                            request_token_params={'scope': ('email, user_friends, friends_location, user_location, read_stream ')}
)


@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_token')


def pop_login_session():
    session.pop('logged_in', None)
    session.pop('facebook_token', None)


@app.route("/facebook_login", methods=['POST', 'GET'])
def facebook_login():
#    if session.has_key('facebook_oauth_tokens'):
#        del session['facebook_oauth_tokens']

    return facebook.authorize(callback=url_for('facebook_authorized',
                                               next='enterdate',
                                               _external=True))


@app.route("/facebook_authorized")
@facebook.authorized_handler
def facebook_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None or 'access_token' not in resp:
        return redirect(next_url)

    session['logged_in'] = True
    session['facebook_token'] = (resp['access_token'], '')

    return redirect(next_url)


@app.route("/logout")
def logout():
    pop_login_session()
    return redirect(url_for('index'))


# ######

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404