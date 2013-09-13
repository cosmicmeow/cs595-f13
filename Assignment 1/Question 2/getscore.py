from bs4 import BeautifulSoup
import urllib2
import sys
import time

# take in arguments
school = sys.argv[1]
minutes = sys.argv[2]
uri = sys.argv[3]

# check if there are 4 parameters passing down
if len(sys.argv) == 4:
	openfile = urllib2.urlopen(uri)
	html = openfile.read()
	openfile.close()

	soup = BeautifulSoup(html)

	# find the class mod-content (node for each game played)
	for game in soup.find_all('div', attrs = {'class':'mod-content'}):

		# if the name of the school is found within the node
		if school in game.get_text():
			visitor = game.find_all('p', attrs = {'class':'team visitor'})
			visitor_name = visitor.find_all('a').text
			visitor_score = visitor.find_all('a').text
			print (visitor_name)
			print (": " + visitor_score + "\n")

			home = game.find_all('p', attrs = {'class':'team home'})
			home_name = home.find_all('a').text
			home_score = visitor.find_all('a').text
			print (home_name)
			print (": " + home_score + "\n")

	time.sleep(minutes)


else:
	print ("Usage: " + sys.argv[0] + "<school> <time> <URI>")


