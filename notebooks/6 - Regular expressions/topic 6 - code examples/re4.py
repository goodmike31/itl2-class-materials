import re

#do two matches
res1 = re.search('a.*b','hat')
res2 = re.search('a.*b','nab')

#evaluate results of both matches
for s,r in [('hat',res1),('nab',res2)]:
	if r:            #simple if test
		print(s,"matches 'a.*b'")
		print("r is a match object")
	else:
		print(s,"does not match 'a.*b'")
		print("r is None")
	if r == False:   #does match simply fail?
		print('r == False')
	else:
		print('r != False')
	if r == None:    #is match a None object?
		print('r == None')
	else:
		print('r != None')

