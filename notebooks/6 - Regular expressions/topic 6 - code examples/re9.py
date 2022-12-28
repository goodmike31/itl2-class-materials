import sys,re

#do a match
m = re.search('(.*)b(.*)',sys.argv[1])
if m:               #if it succeeds, print...
	#the whole match
	print('all: "',m.group(),'"',sep='')
	#the first part
	print('group 1: "',m.group(1),'"',sep='')
	#the second part
	print('group 2: "',m.group(2),'"',sep='')

