import re,sys

if re.search('ab',sys.argv[1]):
	print('a match')
else:
	print('no match')

