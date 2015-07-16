import markov
from utils import utils
import random
import json
from rtmbot import client

outputs = []
alert_phrases = [u'!gilhooly', u'!bryan', u'!brian', u'!bryam']
command_dispatch = {
    u'stats': markov.stats,
    u'image': utils.image_search,
    u'help': utils.help
}


def process_message(data):
    print data
    alert, _, message = data['text'].partition(u' ')
    if alert not in alert_phrases:
        print 'just listening'
        markov.add_to_brain(unicode(data['text']), 2, True)
        return
    command, _, args = message.partition(u' ')
    if command in command_dispatch.keys():
        outputs.append([u"C07HXBJ79", command_dispatch[command](args)])
        return
    markov.add_to_brain(message, 2, True)
    outputs.append([u"C07HXBJ79", markov.generate_sentence(message, 2,
                                                           max_words=10000)])

# def process_hello(data):
#     print(data)
#     outputs.append([u"C07HXBJ79", u"Greetings techie scum"])

possible_greetings = [
    u'{} is back... Greetings techie scum..',
    u'If you have to hang out at my shop {}, can you at least not sit in front of the door?',
    u'How many times do I have to tell you {}, stay away from the fucking door'
]
possible_goodbyes = [
    u'Get out of my shop {}', u'About time that {} leaves..',
    u'{} was the worst techie anyway {}. The rest of you tie for second worst.',
    u"Get away from my shop {} and don't come back"
]


def process_presence_change(data):
    print(data)
    print client
    users = json.loads(
            client.api_call('users.list'))['members']
    print users
    if data['user'] == u'U07KW1M6U':
        return
    if data['presence'] == u'active':
        outputs.append([u"C07HXBJ79", random.choice(possible_greetings).format(
            data['user'])])
    if data['presence'] == u'away':
        outputs.append([u"C07HXBJ79", random.choice(possible_greetings).format(
            data['user'])])
