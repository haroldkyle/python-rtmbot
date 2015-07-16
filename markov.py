# inspired by and borrowed from
# https://github.com/ericflo/yourmomdotcom/blob/master/yourmomdotcom.py

from collections import defaultdict
from datetime import datetime
import codecs
import random

markov = defaultdict(list)
start_time = datetime.utcnow()
STOP_WORD = "\n"


def add_to_brain(msg, chain_length, write_to_file=False):
    if write_to_file:
        f = codecs.open('dillingham_markov.txt', 'a', 'utf-8')
        f.write(msg + '\n')
        f.close()
    buf = [STOP_WORD] * chain_length
    for word in msg.split():
        markov[tuple(buf)].append(word)
        del buf[0]
        buf.append(word)
    markov[tuple(buf)].append(STOP_WORD)


def generate_sentence(msg, chain_length, max_words=10000):
    buf = msg.split()[:chain_length]
    if len(msg.split()) > chain_length:
        message = buf[:]
    else:
        message = []
        for i in xrange(chain_length):
            message.append(random.choice(markov[random.choice(markov.keys())]))
    for i in xrange(max_words):
        try:
            next_word = random.choice(markov[tuple(buf)])
        except IndexError:
            continue
        if next_word == STOP_WORD:
            break
        message.append(next_word)
        del buf[0]
        buf.append(next_word)
    return ' '.join(message)


def stats(args=None):
    total_count = 0
    for k, v in markov.iteritems():
        total_count += len(v)
    total_run_time = datetime.utcnow() - start_time
    stats = 'Number of keys: {}\n Total lengh of chains: {}\n Total run time: {}\n'.format(
        len(markov.keys()), total_count, total_run_time)
    return stats
