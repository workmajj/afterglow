#!/usr/bin/env python

import re
import urllib2

from bs4 import BeautifulSoup

page = urllib2.urlopen('https://www.instagram.com/workmajj/')
soup = BeautifulSoup(page, 'html.parser')

for anchor in soup.find_all('script', string=re.compile('window._sharedData')):
    print anchor.contents[0]
