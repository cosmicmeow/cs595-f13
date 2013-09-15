#!/usr/bin/python
# -*- coding: utf-8 -*-
#BS4 docs http://www.crummy.com/software/BeautifulSoup/bs4/doc/
#find the score http://stackoverflow.com/questions/8993854/is-there-innertext-equivalent-in-beautifulsoup-python

import urllib2
import sys
from bs4 import BeautifulSoup

#test
redditFile = urllib2.urlopen("http://scores.espn.go.com/ncf/scoreboard?confId=80&seasonYear=2013&seasonType=2&weekNumber=2")
redditHtml = redditFile.read()
redditFile.close()
soup = BeautifulSoup(redditHtml)
soup.prettify()
print "goodbye world"

for links in soup.html.bodyfindAll('div'):
	print links.get('class')

print "hello world"