import sys,re

m = re.search('(.*)b(.*)',sys.argv[1])
if m:
	print('all: "',m.group(),'"',sep='')
	print('group 1: "',m.group(1),'"',sep='')
	print('group 1 start:',m.start(1))
	print('group 1 end:',m.end(1))
	print('group 2: "',m.group(2),'"',sep='')
	print('group 2 start:',m.start(2))
	print('group 2 end:',m.end(2))

