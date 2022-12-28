import re,sys

#is some element in string a consonant?
def consonant(s,i):
	letter = s[i]
	if letter in 'aeiou':
		return False
	elif letter == 'y' and i == 0:
		return True
	elif letter == 'y' and consonant(s,i-1):
		return False
	else:
		return True

def cv(w):      #convert string to Cs and Vs
	res = ''
	for i in range(len(w)):
		if consonant(w,i):
			res += 'C'
		else:
			res += 'V'
	return res

def measure(w): #returns measure of a string
	cvword = cv(w)
	vcs = re.findall('VC',cvword)
	return len(vcs)

#general rule framework
def rule(c,e,r,w):
	m = re.search('^(.*)'+e+'$',w)
	if m:
		s = m.group(1)	
		if c(s):
			return s+r
	return None

