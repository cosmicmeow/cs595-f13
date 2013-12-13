import feedfilter
import docclass
import feedparser

cl=docclass.classifier(docclass.getwords) 
cl.setdb('learn.db')
#feedfilter.read('learnprogramming.xml',cl)

myfeed = feedparser.parse('learnprogramming2.xml')


# train data manually -- 50 items blergh!!!
# categories = general, java, c, cpp, csharp, python, sql, others

categories = ['general', 'java', 'c', 'cpp', 'csharp', 'python', 'sql', 'others']
cl.train(myfeed.entries[0].title, 'others')
cl.train(myfeed.entries[1].title, 'general')
cl.train(myfeed.entries[2].title, 'general')
cl.train(myfeed.entries[3].title, 'general')
cl.train(myfeed.entries[4].title, 'c')
cl.train(myfeed.entries[5].title, 'java')
cl.train(myfeed.entries[6].title, 'others')
cl.train(myfeed.entries[7].title, 'java')
cl.train(myfeed.entries[8].title, 'general')
cl.train(myfeed.entries[9].title, 'cpp')
cl.train(myfeed.entries[10].title, 'csharp')
cl.train(myfeed.entries[11].title, 'java')
cl.train(myfeed.entries[12].title, 'general')
cl.train(myfeed.entries[13].title, 'general')
cl.train(myfeed.entries[14].title, 'general')
cl.train(myfeed.entries[15].title, 'general')
cl.train(myfeed.entries[16].title, 'python')
cl.train(myfeed.entries[17].title, 'cpp')
cl.train(myfeed.entries[18].title, 'c')
cl.train(myfeed.entries[19].title, 'others')
cl.train(myfeed.entries[20].title, 'cpp')
cl.train(myfeed.entries[21].title, 'java')
cl.train(myfeed.entries[22].title, 'others')
cl.train(myfeed.entries[23].title, 'python')
cl.train(myfeed.entries[24].title, 'python')
cl.train(myfeed.entries[25].title, 'java')
cl.train(myfeed.entries[26].title, 'general')
cl.train(myfeed.entries[27].title, 'general')
cl.train(myfeed.entries[28].title, 'c')
cl.train(myfeed.entries[29].title, 'general')
cl.train(myfeed.entries[30].title, 'general')
cl.train(myfeed.entries[31].title, 'general')
cl.train(myfeed.entries[32].title, 'c')
cl.train(myfeed.entries[33].title, 'c')
cl.train(myfeed.entries[34].title, 'sql')
cl.train(myfeed.entries[35].title, 'others')
cl.train(myfeed.entries[36].title, 'others')
cl.train(myfeed.entries[37].title, 'cpp')
cl.train(myfeed.entries[38].title, 'general')
cl.train(myfeed.entries[39].title, 'general')
cl.train(myfeed.entries[40].title, 'others')
cl.train(myfeed.entries[41].title, 'cpp')
cl.train(myfeed.entries[42].title, 'general')
cl.train(myfeed.entries[43].title, 'general')
cl.train(myfeed.entries[44].title, 'general')
cl.train(myfeed.entries[43].title, 'general')
cl.train(myfeed.entries[45].title, 'java')
cl.train(myfeed.entries[46].title, 'general')
cl.train(myfeed.entries[47].title, 'python')
cl.train(myfeed.entries[48].title, 'python')
cl.train(myfeed.entries[49].title, 'java')



cl = docclass.fisherclassifier(docclass.getwords)

for i in range(50, 100):
	label = cl.classify(myfeed.entries[i].title)
	print myfeed.entries[i].title + ': ' + label

for i in range(50, 100):
	#for cat in categories:
	print cl.cprob(myfeed.entries[i].title, 'general')