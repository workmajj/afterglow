#!/usr/bin/env python

import json
import re
import urllib
import urllib2

from bs4 import BeautifulSoup

page = urllib2.urlopen('https://www.instagram.com/workmajj/')
soup = BeautifulSoup(page, 'html.parser')

# TODO: assert page structure
anchors = soup.find_all('script', string=re.compile('window._sharedData'))
content = anchors[0].contents[0]

left = content.find('{')
right = content.rfind('}')
json = json.loads(content[left:right+1])

try:
    for node in json['entry_data']['ProfilePage'][0]['user']['media']['nodes']:
        if node['is_video']:
            continue
        f = 'tmp/' + str(int(node['date'])) + '+' + str(node['code']) + '.jpg'
        print urllib.urlretrieve(node['display_src'], f)
except KeyError:
    pass # TODO: assert json structure
