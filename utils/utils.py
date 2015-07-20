import urllib2
import json
import client


def help(args, data=None):
    statement = 'Welcome to Brian Gilhooly bot!\n\n I have many useful features.\n\n Type !gilhooly or !brian to talk to me\n\n Type !gilhooly image followed by a search term to have me fetch an image from Google for you\n\n Type !gilhooly present to see which users are active'
    return statement


def image_search(args=None, data=None):
    if data['user'] == u'U07RGECJ1':
        return u'http://files.disappearednews.com/images/8b0e9098d968_EC08/Varady1.jpg'
    args = args.replace(u' ', u'%20')
    fetcher = urllib2.build_opener()
    startIndex = u'0'
    searchUrl = u"http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + args + u"&start=" + startIndex
    f = fetcher.open(searchUrl)
    deserialized_output = json.loads(f.read())
    return deserialized_output['responseData']['results'][0]['unescapedUrl']


def get_present_users(args=None, data=None):
    users = client.get_users()
    present_users = []
    # print all_users
    for user in users:
        if user['id'] == u'U07KW1M6U':
            continue
        presence = client.get_presence(user['id'])
        if presence['presence'] == 'active':
            present_users.append(user['real_name'])
    return u', '.join(present_users)
