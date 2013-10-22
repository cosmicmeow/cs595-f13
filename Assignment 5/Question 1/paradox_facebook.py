import sys
from xml.dom.minidom import parseString

file = open('Lookmai_Rattana_1382401437.graphml')
data = file.read()
file.close()

outfile = open('paradox_facebook_FC.txt', 'w')
dom = parseString(data)
total = 0
friends = 0
for element in dom.getElementsByTagName('data'):
	if (element.attributes['key'].value == 'name'):
		total = total+1
		
	if (element.attributes['key'].value == 'friend_count'):
		friends = friends + 1
		count = element.childNodes[0].data

		outfile.write(str(friends) + ',' + count + '\n')

outfile.write ('Me,' + str(total))
outfile.close()