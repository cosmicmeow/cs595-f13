#!/usr/bin/python
# -*- coding: utf-8 -*-
#BS4 docs http://www.crummy.com/software/BeautifulSoup/bs4/doc/


import urllib2
import sys
from bs4 import BeautifulSoup
#  1. takes one argument, like "Old Dominion" or "Virginia Tech"
# 2. takes another argument specified in seconds (e.g., "60" for
#     one minute).
#  3. takes a URI as a third argument, such as:
#     http://scores.espn.go.com/ncf/scoreboard?confId=80&seasonYear=2013&seasonType=2&weekNumber=2
#     or
#     http://scores.espn.go.com/ncf/scoreboard?confId=80&seasonYear=2013&seasonType=2&weekNumber=1
#     or
#     http://scores.espn.go.com/ncf/scoreboard?confId=80&seasonYear=2012&seasonType=2&weekNumber=1
#     etc.
#  4. downloads the URI, finds the game corresponding to the team
#     argument, prints out the current score (e.g., "Old Dominion 38,
#     East Carolina 52), sleeps for the specified seconds, and then
#     repeats (until control-C is hit).

#team = sys.argv[1]
#time = sys.argv[2]
#uri  = sys.argv[3]

def scores(school, time, uri):
	print school
	print time
	print uri
	response = urllib2.urlopen(uri)
	responseRead = response.read()
	response.close()
	soup = BeautifulSoup(responseRead)
	for links in soup.find_all('div',{'class' :'final'}):
		print links #(links.get('final'))





#test
redditFile = urllib2.urlopen("http://scores.espn.go.com/ncf/scoreboard?confId=80&seasonYear=2013&seasonType=2&weekNumber=1")
redditHtml = redditFile.read()
redditFile.close()
soup = BeautifulSoup(redditHtml)

for visitingTeam in soup.html.body.findAll('div',{'class' : 'team visitor'}):
#first anchor after the <div> is the name of the visiting team
	visitingTeamName=str(visitingTeam.find('a').get('title')).strip()
	print visitingTeamsName
#<li class="final" id="332412579-aTotal">20</li>
	visitingScore=visitingTeam.find('li', {'class' : 'final'}).string.strip()
#create a parallel list for the visiting teams
	visitingTeamsRec[gameNumber] = visitingTeamName + " " + visitingScore
	gameNumber=gameNumber+1
	print visitingTeamsRec




#scores("Old Dominion", 60, "http://scores.espn.go.com/ncf/scoreboard?confId=80&seasonYear=2013&seasonType=2&weekNumber=1")

response = urllib2.urlopen('http://www.cs.odu.edu/~hany')
html = response.read()
#print html
# do somethingrak
response.close()

