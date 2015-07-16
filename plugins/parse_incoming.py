from markov import add_to_brain, generate_sentence, markov_stats
outputs = []


def process_message(data):
    print data
    if unicode(unicode(data['text']).partition(u' ')[0]) == u'!gilhooly':
        message = unicode(unicode(data['text'])).replace(u'!gilhooly ', u'')
        if message.partition(u' ')[0] == u'stats':
            outputs.append([u"C07HXBJ79", markov_stats()])
            return
        add_to_brain(message, 2, True)
        outputs.append([u"C07HXBJ79", generate_sentence(message, 2,
                                                        max_words=10000)])
    else:
        add_to_brain(unicode(data['text']), 2, True)
    # outputs.append(["C07HXBJ79", "Test response"])


def process_hello(data):
    print(data)
    outputs.append([u"C07HXBJ79", u"Greetings techie scum"])


def process_presence_change(data):
    print(data)
    # if data['presence'] == 'active':
