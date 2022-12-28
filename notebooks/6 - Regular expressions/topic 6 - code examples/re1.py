import sys

def mymatch(s):      #a and then b
	i = 0
	#flag to keep track of
	#whether we see an 'a'
	aFlag = False
	while i < len(s):
		if s[i] == 'a':
			aFlag = True
			break
		i += 1
	#look for 'b' where we left off
	while i < len(s):
		if s[i] == 'b':
			#if we find 'b', return True of
			#False depending on whether we
			#previously saw 'a'
			return aFlag
		i += 1
	#if all that fails, return False
	return False

print(mymatch(sys.argv[1]))

