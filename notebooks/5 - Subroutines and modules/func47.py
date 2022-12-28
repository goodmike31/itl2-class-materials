#function to split into sentences
def getsentences(t):
	splitters = '.?!' #characters to split on
	ss = []           #where we put sentences
	i = 0
	#go character by character
	while i < len(t):
		s = ''         #reset current sentence
		#read to end of text orend of sentence
		while i < len(t) and \
			t[i] not in splitters:
				s += t[i]
				i += 1
		#if text isn't over, current character
		#is splitter and should be appended
		if i < len(t):
			s += t[i]
		i += 1         #go on to next character
		ss.append(s)   #add current sentence
	return ss

#remove non-space breaks and trim spaces
def makespaces(t):
	breaks = '\n\t'   #characters to convert
	r1 = ''           #output of 1st convert
	i = 0
	#go through 1 by 1
	while i < len(t):
		#current char should be converted?
		if t[i] in breaks:
			r1 += ' '
		else:
			r1 += t[i]
		i += 1
	#eliminate space after another space
	r2 = r1[0]
	i = 1             #start at 2nd char
	#go through the whole thing
	while i < len(r1):
		#check for two spaces in a row
		if r1[i] == ' ' and \
			r2[len(r2)-1] == ' ':
				i += 1   #skip if so
				continue
		#otherwise, append current char
		else:
			r2 += r1[i]
		i += 1
	return r2

#remove spaces at edges of strings
def trimspaces(t):
	#result list
	r1 = []
	#go through one by one
	for s in t:
		#if first char is a space
		if s[0] == ' ':
			s = s[1:]
		slast = len(s) - 1
		#if last char is a space
		if len(s) > 0 and s[slast] == ' ':
			s = s[:slast]
		r1.append(s)
	#prune empty sentences
	r2 = []
	#go through one by one
	for s in r1:
		#check if sentence is empty
		if len(s) > 0:
			r2.append(s)
	return r2

