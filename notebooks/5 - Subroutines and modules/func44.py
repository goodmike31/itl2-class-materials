import func43

#function to read in file
#and prune header info
def readfile(filename):
	f = open(filename,'r')
	text = f.read()
	f.close()
	text = text[10841:]
	return text

#read in file and strip header
txt = readfile('alice.txt')
#split into sentences
s = func43.getsentences(txt)
#print first 10 sentences
for i in range(10):
	print(i,s[i])

