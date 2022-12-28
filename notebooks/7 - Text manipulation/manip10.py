import re,sys

#checks if some element in
#a string is a consonant
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

#returns the measure of a string
def measure(w):
	cvword = cv(w)
	vcs = re.findall('VC',cvword)
	return len(vcs)

def stem(w):  #stemming code frame
	return w

word = sys.argv[1]
print(word)
print(cv(word))
print(measure(word))

