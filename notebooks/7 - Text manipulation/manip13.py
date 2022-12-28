import re,sys,manip12

def m1cond(x):   #condition: m > 0
	if manip12.measure(x) > 0:
		return True
	return False

def edrule(w):   #sample rule for -ed
	x = manip12.rule(m1cond, 'ed', '', w)
	return x

def stem(w):     #stemming with -ed rule
	res = edrule(w)
	if res:
		return res
	return w

word = sys.argv[1]
print(word)
print(stem(word))

