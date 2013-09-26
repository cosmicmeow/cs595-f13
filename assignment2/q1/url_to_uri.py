import subprocess
import requests

'''for x in range(9):
	y += x
	print y
'''
f = open('workfile', 'r')
t = open('output', 'w')
l = f.read().splitlines()
#print l

for each in l:
  	try:
		r= requests.get(each)
		if (r.status_code==200):
			print r.url 
			t.write(r.url+"\n")
	except:
		pass

t.close()

	#shell_command = 'curl" -I -L %s"'%(each)
	#subp = subprocess.Popen(['curl',  '-L', '-I', each],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	#curlstdout, curlstderr = subp.communicate()

	#op = str(curlstdout)
	#print op

	#event = Popen(shell_command, shell=True, stdin=PIPE, stdout=PIPE, 
    #stderr=STDOUT)
	#output = event.communicate()
	#print output + "\n"
	#print "I can program in " + each