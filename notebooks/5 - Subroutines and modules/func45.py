import func43

#function to read in file, prune header info
def readfile(filename):
	f = open(filename,'r')
	text = f.read()
	f.close()
	text = text[10841:]
	return text

#remove non-space breaks and trim spaces
def makespaces(t):
	breaks = '\n\t'    #characters to convert
	r1 = ''            #output of 1st convert
	i = 0
	while i < len(t):  #go through 1 by 1
		#current char should be converted?
		if t[i] in breaks:
			r1 += ' '
		else:
			r1 += t[i]
		i += 1
	#eliminate space after another space
	r2 = r1[0]
	i = 1              #start at 2nd char
	#go through whole thing
	while i < len(r1):
		#check for two spaces in a row
		if r1[i] == ' ' and \
			r2[len(r2)-1] == ' ':
				#skip if so
				i += 1
				continue
		#otherwise, append current char
		else:
			r2 += r1[i]
		i += 1
	return r2

#read in file and strip header
txt = readfile('alice.txt')
#remove non-space breaks and trim spaces
cleanedtext = makespaces(txt)
#split into sentences
s = func43.getsentences(cleanedtext)
#print first 10 sentences
for i in range(10):
	print('\n',i,': ',s[i],sep='')

