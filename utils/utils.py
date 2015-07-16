import urllib2
import json


def help(args):
    statement = 'Welcome to Brian Gilhooly bot!\n\n I have many useful features.\n\n Type !gilhooly or !brian to talk to me\n\n Type !image followed by a search term to have me fetch an image from Google for you\n'
    return statement


def image_search(args=None):
    args = args.replace(u' ', u'%20')
    fetcher = urllib2.build_opener()
    startIndex = u'0'
    searchUrl = u"http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + args + u"&start=" + startIndex
    print u'searching ' + searchUrl
    f = fetcher.open(searchUrl)
    deserialized_output = json.loads(f.read())
    return deserialized_output['responseData']['results'][0]['unescapedUrl']
