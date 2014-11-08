
import facepy

# Set up facebook
#~ # Application Logi
app_id = 243821869114636
app_secret = '24dbc63beb9cf0577aaee5a5e1b8208a'
post_login_url = "http://0.0.0.0:8080/"
auth_head = "http://0.0.0.0:8080/?#access_token=CAADdwTPlpQwBANk4XM3wsvfofSG1ZC0DnTzLdLUcJk74dEQGDLAPZCyTjf4M9ZBa1Y3AwjX0AZBullYsAk7m5gEepHQMxfiwjIsiEZCTQSPFLzlMx9N5hOzXSn83dSwkJ8xZASRobyDqqtrvdCnP62hhpZBKa36tygUkTWQP2vEyukEq5hRYO98dpJ1ZBiUWtsX74txCvjbVXGH13BnEhO8jtvagZC3OhmMoZD&expires_in=4904"

def global_login():
    oauth_access_token = facepy.utils.get_application_access_token(app_id, app_secret)
    return facepy.GraphAPI(oauth_access_token)

def user_login():
    #print "http://www.facebook.com/dialog/oauth?" + "client_id=" + str(app_id) + "&redirect_uri=" + post_login_url + "&scope=friends_hometown&response_type=token" 
    #webbrowser.open("http://www.facebook.com/dialog/oauth?" + "client_id=" + str(app_id) + "&redirect_uri=" + post_login_url + "&scope=read_stream&response_type=token" )
    acc_token = auth_head.split('=')[1].split('&')[0]
    ext_access_token, expires_on= facepy.utils.get_extended_access_token(acc_token,app_id, app_secret)
    return facepy.GraphAPI(ext_access_token)
