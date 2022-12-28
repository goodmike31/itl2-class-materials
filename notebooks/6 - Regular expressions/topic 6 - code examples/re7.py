import re,sys

#find all matches
res = re.findall('a',sys.argv[1])
if res:                    #if at least 1
	print('match:',res)     #print list
else:
	print('no match:',res)  #print empty list

