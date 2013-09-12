#Q2

from bs4 import BeautifulSoup
import urllib2


school = ""
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
for teamNames in soup.html.body.find_all('div',{'class':'final-state'}):
	print teamNames
	print teamNames.get('div',{'class':'team visitor'})
	print teamNames.get('div',{'class':'team home'})
#team-home
#team-visitor 