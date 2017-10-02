#!/usr/bin/env python3
"""
Reimagine the last message as if it were said by Snoop Dogg himself.
"""

import json
import requests
from bs4 import BeautifulSoup


__author__ = 'iandioch'
COMMAND = '.kanye'
KANYEREST_URL = 'http://kanyerest.xyz/api/album/'
ALBUMS = ['graduation']
WORDS = set()

def load():
	for album in ALBUMS:
		url = KANYEREST_URL + album
		r = requests.post(url)
		data = json.loads(r.text)
		for song in data['result']:
			WORDS = WORDS.union(song['lyrics'])
	print(WORDS)

def kanye(text):
	return text


def main(bot, author_id, message, thread_id, thread_type, **kwargs):
    prev_message = bot.fetchThreadMessages(thread_id=thread_id, limit=2)[1]
    bot.sendMessage(kanye(prev_message.text),
                    thread_id=thread_id,
                    thread_type=thread_type)

# To be run at boot
load()
