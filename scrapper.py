import facebook_helper as fb


def grab_friends():
    g = fb.user_login()

    res = g.get('me/friends', page=True)
    data = []
    for page in res:
        data += page["data"]

    for friend in data:
        yield g.get(str(friend['id']))
