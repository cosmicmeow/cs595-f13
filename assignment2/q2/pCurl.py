#import pycurl
import requests

odu_memento = "http://mementoproxy.cs.odu.edu/aggr/timemap/link/"
f = open('final_uri_list.txt', 'r')
t = open('memento.txt', 'w')
l = f.read().splitlines()
#print l
num = 0
for each in l:
  	try:
  		query = odu_memento+ each
  		#print each
  		num = num + 1
  		print num
		r= requests.get(query)
		if (r.status_code==200):
			print r.url 
			search = r.text
			count = [i for i in range(len(search)) if search.startswith('memento', i)]
			t.write(each+" "+ len(count) +"\n")
		elif (r.status_code==404):
			print each+" 0\n"
			t.write(each+" 0\n")
	except:
		pass
