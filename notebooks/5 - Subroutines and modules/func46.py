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
	#go through the whole thing
	while i < len(r1):
		#check for two spaces in a row
		if r1[i] == ' ' and \
			r2[len(r2)-1] == ' ':
				i += 1    #skip if so
				continue
		#otherwise, append current char
		else:
			r2 += r1[i]
		i += 1
	return r2

#remove spaces at edges of strings
def trimspaces(t):
	r1 = []            #result list
	for s in t:        #go through 1 by 1
		#if first char is a space
		if s[0] == ' ':
			s = s[1:]
		slast = len(s) - 1
		#if last char is a space
		if len(s) > 0 and s[slast] == ' ':
			s = s[:slast]
		r1.append(s)
	r2 = []            #prune empty sentences
	for s in r1:       #go through one by one
		#check if sentence is empty
		if len(s) > 0:
			r2.append(s)
	return r2

#read in file and strip header
txt = readfile('alice.txt')
#remove non-space breaks and extra spaces
cleanedtext = makespaces(txt)
#split into sentences
ss = func43.getsentences(cleanedtext)
#trim edges of sentences
ts = trimspaces(ss)
#print first 10 sentences
for i in range(10):
	print('\n',i,': %',ts[i],'%',sep='')

