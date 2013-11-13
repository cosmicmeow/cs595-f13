#!/usr/local/bin/python3

import json

infile = open("zachary.dat", 'r')
lines = infile.readlines()
infile.close()

outfile = open("karateclub.json", 'w')

# create dictionary for each nodes and their respective links(edges)
dict = {"nodes" : [], "links" : []}


#count nuumber of nodes
count = 0

# ignore the first 41 lines from the data file
for line in lines[41:]:
	num = count + 1
	node = {"number" : str(num)}
	dict["nodes"].append(node)
	connections = line.split()

	for i in range(0, len(connections)):
		value = int(connections[i])
		if value != 0:
			link = {"source" : num, "target"  : i, "value" : int(value)}
			dict["links"].append(link)

	count = count + 1

# pretty printing json file with indent and seperators : D
output = json.dumps(dict, indent=4, separators=(',', ': '))
outfile.write(output)
outfile.close()