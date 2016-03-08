#!/usr/bin/env python

import json
import re
import urllib
import urllib2

from bs4 import BeautifulSoup

IG_BASE_URL = 'https://www.instagram.com'
IG_JSON_VAR = 'window._sharedData'

# FIXME: assert page and json structure

def get_json(user):
    page = urllib2.urlopen('{}/{}/'.format(IG_BASE_URL, user))
    soup = BeautifulSoup(page, 'html.parser')

    anchors = soup.find_all('script', string=re.compile(IG_JSON_VAR))
    content = anchors[0].contents[0]

    left = content.find('{')
    right = content.rfind('}')

    return json.loads(content[left:right+1])

def get_images(json):
    for node in json['entry_data']['ProfilePage'][0]['user']['media']['nodes']:
        if node['is_video']:
            continue

        f = 'tmp/{}+{}.jpg'.format(int(node['date']), node['code'])
        print urllib.urlretrieve(node['display_src'], f)

def main():
        json = get_json('workmajj') # FIXME
        get_images(json)

if __name__ == '__main__':
    main()
