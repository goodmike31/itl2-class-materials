import re,sys,manip12

def m1cond(x):   #condition: m > 0
	if manip12.measure(x) > 0:
		return True
	return False

def step1a(w):
	return w

def step1b(w):
	return w

def step1c(w):
	return w

def step2(w):
	return w

def step3(w):
	return w

def step4(w):
	return w

def step5a(w):
	return w

def step5b(w):
	return w

def stem(w):     #stemming with blocks
	s1a = step1a(w)
	s1b = step1b(s1a)
	s1c = step1c(s1b)
	s2 = step2(s1c)
	s3 = step3(s2)
	s4 = step4(s3)
	s5a = step5a(s4)
	s5b = step5b(s5a)
	return s5b

word = sys.argv[1]
print(word)
print(stem(word))

