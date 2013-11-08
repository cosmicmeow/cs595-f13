#!/usr/local/bin/python3

import json

infile = open("zachary.dat")
lines = infile.readlines()
infile.close()

dict = {}
dict["nodes"] = []
dict["links"] = []

num = 0

# ignore the first 7 lines (0-6) and read up to the next 34 lines for connections
for line in lines[41:]:
	num = num + 1
	node = {"number" : str(num)}
	dict['nodes'].append(node)
	connections = line.split()

	for x in range(len(connections)):
		if connections[x] != "0":
			link = {"source" : num, "target"  : x, "weight" : int(connections[x])}
			dict['links'].append(link)

	num = num + 1

print(json.dumbs(dict))