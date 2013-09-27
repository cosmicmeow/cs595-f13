import re
import sys
import requests

memento = 'http://mementoproxy.cs.odu.edu/aggr/timemap/link/'


if __name__ == "__main__":

    inFile = sys.argv[1]
    
    links_list = open(inFile)
    outFile = open('memento.txt', 'w')

    for link in links_list:
		try:
	  		query = memento + link

			r = requests.get(query)
			if (r.status_code == 200):
				search = r.text
				memento_count = [i for i in range(len(search)) if search.startswith('memento', i)]
				outFile.write(link + " " + len(memento_count) +"\n")
			else:
				print link + " 0\n"
				outFile.write(link + " 0\n")
		except:
				pass

    links_list.close()
