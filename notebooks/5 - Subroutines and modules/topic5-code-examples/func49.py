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
#dictionary to keep track of counts
counts = {}
#go through all sentences
for s in ts:
	slength = len(s.split())  #count words
	#add 1 to relevant count in dictionary
	if slength in counts:
		counts[slength] += 1
	else:
		counts[slength] = 1
for c in sorted(counts):     #print counts
	print(c,counts[c])

