import func47

#function to read in file, prune header info
def readfile(filename):
	f = open(filename,'r')
	text = f.read()
	f.close()
	text = text[10841:]
	return text

#read in file and strip header
txt = readfile('alice.txt')
#remove non-space breaks and extra spaces
cleanedtext = func47.makespaces(txt)
#split into sentences
ss = func47.getsentences(cleanedtext)
#trim edges of sentences
ts = func47.trimspaces(ss)
#print first 10 sentences
for i in range(10):
	print('\n',i,': %',ts[i],'%',sep='')

