#Stanley Zheng
#CS495/595 Assignment 1
#Q2 Parse and grab scores from ESPN website
#usage  python ./q2.py team time website
#sources
#using .encode('utf-8') to solve ascii errors 
	#http://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20
#Hany ~ office hours help
	#jsoup
from bs4 import BeautifulSoup
import urllib2
import sys
import time

#final system args
#school = sys.argv[1]
#time = sys.argv[2]
#website = sys.argv[3]
school = "Florida Atl"
time = 0
website = "http://scores.espn.go.com/ncf/scoreboard?confId=80&seasonYear=2013&seasonType=2&weekNumber=2"

openFile = urllib2.urlopen(website)
getHtml = openFile.read()
openFile.close()
soup = BeautifulSoup(getHtml)
#for scores in soup.html.body.find_all('li', {'class':'final'}):
#	print scores.text
#for teamNames in soup.html.body.find_all('a'):
#	print teamNames.get('title')
for teamNames in soup.html.body.find_all('div',{'class':'mod-content'}):
	if school in teamNames.get_text():
		print school
	#visitors
	 	visitor =teamNames.find_all('div',{'class':'team visitor'})
	 	home = teamNames.find_all('div',{'class':'team home'})
	 	#print repr(visitor)
	 	#print repr(home)

	 	#for scores in home.find_all("scores"):
	 	#	print "scores"
	 	print repr(home)


	# teamNames.prettify().encode('utf-8')
	#print teamNames.get('div',{'class':'team visitor'})
	#print teamNames.get('div',{'class':'team home'})
#team-home
#team-visitor 