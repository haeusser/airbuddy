__author__ = 'Philip'

# imports
import sys
import os.path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
from flask import Flask, request, render_template, redirect, url_for, session, \
    request, send_from_directory
from flask_oauth import OAuth




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


@app.route('/enterdate', methods=['POST', 'GET'])
def enterdate():
    form_url = '/wait'
    data = facebook.get('/me').data
    if 'id' in data and 'name' in data:
        user_id = data['id']
        user_name = data['name']
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
                            request_token_params={'scope': ('email, ')}
)


@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_token')


def pop_login_session():
    session.pop('logged_in', None)
    session.pop('facebook_token', None)


@app.route("/facebook_login")
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