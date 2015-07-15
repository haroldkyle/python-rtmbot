from markov import add_to_brain, generate_sentence
outputs = []


def process_message(data):
    print data
    if data['text'].partition(' ')[0] == '!gilhooly':
        message = data['text'].replace('!gilhooly', '')
        add_to_brain(message, 2, True)
        outputs.append(["C07HXBJ79", generate_sentence(message, 2,
                                                       max_words=10000)])
    else:
        add_to_brain(data['text'], 2, True)
    # outputs.append(["C07HXBJ79", "Test response"])


def process_hello(data):
    print data
    outputs.append(["C07HXBJ79", "Greetings techie scum"])


def process_presence_change(data):
    print data
    # if data['presence'] == 'active':
