def myF(s):        #this uses _mySplit()
	'''This calculates the number of
	words in a string minus one.

	s -- the string
	'''
	wds = _mySplit(s)
	return len(wds)

def _mySplit(s):   #this is private!
	'''This returns all the words in
	a string except the first.

	This docstring is pointless!
	'''
	ws = s.split()
	return ws[1:]

