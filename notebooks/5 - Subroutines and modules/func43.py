#function to split into sentences
def getsentences(t):
	splitters = '.?!' #characters to split on
	ss = []           #put sentences here
	i = 0
	#go character by character
	while i < len(t):
		s = ''         #reset current sentence
		#read until the end of the text or
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

