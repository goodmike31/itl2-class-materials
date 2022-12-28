import re,sys
from manip12 import *

def m1cond(x):    #condition: m > 0
	if measure(x) > 0:
		return True
	return False

def m2cond(x):    #condition: m > 1
	if measure(x) > 1:
		return True
	return False

def nullcond(x):  #vacuous condition
	return True

def vcond(x):     #condition: contains vowel
	cvform = cv(x)
	if re.search('V',cvform):
		return True
	return False

def step1a(w):
	a = rule(nullcond,'sses','ss',w)
	if a: return a
	b = rule(nullcond,'ies','i',w)
	if b: return b
	c = rule(nullcond,'ss','ss',w)
	if c: return c
	d = rule(nullcond,'s','',w)
	if d: return d
	return w

#specialrule
def specialrule(w):
	cvform = cv(w)
	m = re.search('CC$',cvform)
	if m:
		m2 = re.search('^(.*)([^szl])\\2',w)
		if m2:
			return m2.group(1)+m2.group(2)
	return None

def m1ocond(w):   #m=1 and ends in CV[^xyw]
	cvform = cv(w)
	if measure(cvform) == 1:
		m = re.search('CVC$',cvform)
		if m:
			m2 = re.search('[^xyw]$',w)
			if m2:
				return True
	return False

def special(w):   #special block for ed/ing
	a = rule(nullcond,'at','ate',w)
	if a: return a
	b = rule(nullcond,'bl','ble',w)
	if b: return b
	c = rule(nullcond,'iz','ize',w)
	if c: return c
	d = specialrule(w)
	if d: return d
	e = rule(m1ocond,'','e',w)
	if e: return e
	return w

def step1b(w):
	a = rule(m1cond,'eed','ee',w)
	if a: return a
	b = rule(vcond,'ed','',w)
	if b: return special(b)
	c = rule(vcond,'ing','',w)
	if c: return special(c)
	return w

def step1c(w):
	a = rule(vcond,'y','i',w)
	if a: return a
	return w

def step2(w):
	a = rule(m1cond,'ational','ate',w)
	if a: return a
	b = rule(m1cond,'tional','tion',w)
	if b: return b
	c = rule(m1cond,'enci','ence',w)
	if c: return c
	d = rule(m1cond,'anci','ance',w)
	if d: return d
	e = rule(m1cond,'izer','ize',w)
	if e: return e
	f = rule(m1cond,'abli','able',w)
	if f: return f
	g = rule(m1cond,'alli','al',w)
	if g: return g
	h = rule(m1cond,'entli','ent',w)
	if h: return h
	i = rule(m1cond,'eli','e',w)
	if i: return i
	j = rule(m1cond,'ousli','ous',w)
	if j: return j
	k = rule(m1cond,'ization','ize',w)
	if k: return k
	l = rule(m1cond,'ation','ate',w)
	if l: return l
	m = rule(m1cond,'ator','ate',w)
	if m: return m
	n = rule(m1cond,'alism','al',w)
	if n: return n
	o = rule(m1cond,'iveness','ive',w)
	if o: return o
	p = rule(m1cond,'fulness','ful',w)
	if p: return p
	q = rule(m1cond,'ousness','ous',w)
	if q: return q
	r = rule(m1cond,'aliti','al',w)
	if r: return r
	s = rule(m1cond,'iviti','ive',w)
	if s: return s
	t = rule(m1cond,'biliti','ble',w)
	if t: return t
	return w

def step3(w):
	a = rule(m1cond,'icate','ic',w)
	if a: return a
	b = rule(m1cond,'ative','',w)
	if b: return b
	c = rule(m1cond,'alize','al',w)
	if c: return c
	d = rule(m1cond,'iciti','ic',w)
	if d: return d
	e = rule(m1cond,'ical','ic',w)
	if e: return e
	f = rule(m1cond,'ful','',w)
	if f: return f
	g = rule(m1cond,'ness','',w)
	if g: return g
	return w

def m2stcond(w):  #m > 1 and ends in [st]
	if m2cond(w):
		m = re.search('[st]$',w)
		if m:
			return True
	return False

def step4(w):
	a = rule(m2cond,'al','',w)
	if a: return a
	b = rule(m2cond,'ance','',w)
	if b: return b
	c = rule(m2cond,'ence','',w)
	if c: return c
	d = rule(m2cond,'er','',w)
	if d: return d
	e = rule(m2cond,'ic','',w)
	if e: return e
	f = rule(m2cond,'able','',w)
	if f: return f
	g = rule(m2cond,'ible','',w)
	if g: return g
	h = rule(m2cond,'ant','',w)
	if h: return h
	i = rule(m2cond,'ement','',w)
	if i: return i
	j = rule(m2cond,'ment','',w)
	if j: return j
	k = rule(m2cond,'ent','',w)
	if k: return k
	l = rule(m2stcond,'tion','',w)
	if l: return l
	m = rule(m2cond,'ou','',w)
	if m: return m
	n = rule(m2cond,'ism','',w)
	if n: return n
	o = rule(m2cond,'ate','',w)
	if o: return o
	p = rule(m2cond,'iti','',w)
	if p: return p
	q = rule(m2cond,'ous','',w)
	if q: return q
	r = rule(m2cond,'ive','',w)
	if r: return r
	s = rule(m2cond,'ize','',w)
	if s: return s
	return w

#m = 1 and not *O
def m1notocond(w):
	if measure(w) != 1:
		return False
	cvform = cv(w)
	m = re.search('CVC$',cvform)
	if m:
		m2 = re.search('[wxy]$',w)
		if m2:
			return False
	return True

def step5a(w):
	a = rule(m2cond,'e','',w)
	if a: return a
	b = rule(m1notocond,'e','',w)
	if b: return b
	return w

def step5b(w):
	if m2cond(w):
		m = re.search('(^.*l)(l)$',w)
		if m:
			return m.group(1)
	return w

def stem(w):      #stemming with blocks
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

