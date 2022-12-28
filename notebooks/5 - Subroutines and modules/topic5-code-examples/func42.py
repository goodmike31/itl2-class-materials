#function to read file, prune header info
def readfile(filename):
	f = open(filename,'r')
	text = f.read()
	f.close()
	text = text[10841:]
	return text

#function to split into sentences
def getsentences(t):
	splitters = '.?!' #characters to split on
	ss = []           #put sentences here
	i = 0
	#go character by character
	while i < len(t):
		s = ''         #reset current sentence
		#read to end of text or
		#end of a sentence
		while i < len(t) and \
			t[i] not in splitters:
				s += t[i]
				i += 1
		#if text isn't over, current character
		#is splitter and should be appended
		if i < len(t):
			s += t[i]
		i += 1         #go on to next character
		ss.append(s)   #add sentence to list
	return ss

#read in file and strip header
txt = readfile('alice.txt')
#split into sentences
s = getsentences(txt)
#print first 10 sentences
for i in range(10):
	print(i,s[i])

