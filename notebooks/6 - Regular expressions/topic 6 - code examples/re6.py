import re,sys

#do a match
res = re.search('a.*b',sys.argv[1])
if res: #if match succeeds, print everything
	print("match: '",res.group(),"'",sep='')
	print('starting index:',res.start())
	print('ending index:',res.end())
	print('both indices:',res.span())
else:
	print('no match')

