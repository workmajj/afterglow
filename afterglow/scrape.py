#!/usr/bin/env python

import json
import os
import re
import sys
import urllib
import urllib2

from bs4 import BeautifulSoup

IG_BASE_URL = 'https://www.instagram.com'
IG_JSON_VAR = 'window._sharedData'

def ig_user_to_json(user):
    try:
        page = urllib2.urlopen('{}/{}/'.format(IG_BASE_URL, user))
    except urllib2.HTTPError:
        sys.exit('could not get page for user {}'.format(user))

    # search <script> tags for json var, trim whitespace, and parse

    soup = BeautifulSoup(page, 'html.parser')
    tags = soup.find_all('script', string=re.compile(IG_JSON_VAR))

    if not tags:
        sys.exit('could not find json text on page')

    text = tags[0].contents[0]
    l = text.find('{')
    r = text.rfind('}')

    if l == -1 or r == -1:
        sys.exit('malformed json text on page')

    return json.loads(text[l:r+1])

def get_images(json):
    try:
        nodes = json['entry_data']['ProfilePage'][0]['user']['media']['nodes']
    except KeyError:
        sys.exit('json structure has changed')

    for node in nodes:
        if node['is_video']:
            continue

        f = 'ig/{:.0f}+{}+{}.jpg'.format(node['date'],
            node['owner']['id'], node['code'])

        print urllib.urlretrieve(node['display_src'], f)

def main():
    if len(sys.argv) != 3:
        sys.exit('usage: {} <ig_user> <tmp_dir>'.format(sys.argv[0]))

    if not os.path.isdir(sys.argv[2]):
        sys.exit('{} is not a directory'.format(sys.argv[2]))

    json = ig_user_to_json(sys.argv[1])
    get_images(json)

if __name__ == '__main__':
    main()
