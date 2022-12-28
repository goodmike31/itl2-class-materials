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

#converts string to Cs and Vs
def cv(w):
	res = ''
	for i in range(len(w)):
		if consonant(w,i):
			res += 'C'
		else:
			res += 'V'
	return res

#returns measure of a string
def measure(w):
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

def m1cond(x):   #condition: m > 0
	if measure(x) > 0:
		return True
	return False

#specific sample rule for -ed
def edrule(w):
	x = rule(m1cond, 'ed', '', w)
	return x

def stem(w):     #using -ed rule
	res = edrule(w)
	if res:
		return res
	return w

word = sys.argv[1]
print(word)
print(stem(word))

