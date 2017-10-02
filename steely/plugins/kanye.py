#!/usr/bin/env python3
"""
Reimagine the last message as if it were said by Snoop Dogg himself.
"""

import difflib
import json
import requests
from whoosh.spelling import ListCorrector

__author__ = 'iandioch'
COMMAND = '.kanye'
KANYEREST_URL = 'http://kanyerest.xyz/api/counter'
WORDS = None

def load():
    r = requests.get(KANYEREST_URL)
    data = json.loads(r.text)
    words = sorted(data, key = lambda x: data[x], reverse=True)
    print('Kanye dict is {} words', len(words))
    print(words[:50])
    return (words)

def kanye(text):
    words = text.split()
    if len(words) > 100:
        return 'My greatest pain in life is that I will never be able to see myself perform live.'
    out = []
    for word in words:
        if False or word in WORDS:
            out.append(word)
            continue
        # best_guesses = difflib.get_close_matches(word, WORDS, 1, 0)
        best_guesses = corrector.suggest(word, limit=1, maxdist=5)
        if len(best_guesses) > 0:
            out.append(best_guesses[0])
        else:
            out.append(word)
    return ' '.join(out)


def main(bot, author_id, message, thread_id, thread_type, **kwargs):
    prev_message = bot.fetchThreadMessages(thread_id=thread_id, limit=2)[1]
    bot.sendMessage(kanye(prev_message.text),
                    thread_id=thread_id,
                    thread_type=thread_type)

# To be run at boot
WORDS = load()
corrector = ListCorrector(WORDS)
