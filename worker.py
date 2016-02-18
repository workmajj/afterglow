#!/usr/bin/env python

import json
import re
import urllib
import urllib2

from bs4 import BeautifulSoup

page = urllib2.urlopen('https://www.instagram.com/workmajj/')
soup = BeautifulSoup(page, 'html.parser')

anchors = soup.find_all('script', string=re.compile('window._sharedData'))
content = anchors[0].contents[0]

left = content.find('{');
right = content.rfind('}');

print json.loads(content[left:right+1])
