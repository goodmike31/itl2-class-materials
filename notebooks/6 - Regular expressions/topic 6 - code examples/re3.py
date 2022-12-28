import re,sys

if re.search('a.*b',sys.argv[1]):
	print('a match')
else:
	print('no match')

