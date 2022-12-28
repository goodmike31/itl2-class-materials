import re,sys

#do a match
res = re.search('a.*b',sys.argv[1])
if res:   #if match succeeds, print matching
	print("match: '",res.group(),"'",sep='')
else:
	print('no match')

