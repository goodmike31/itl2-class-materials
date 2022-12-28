import re

#a test string
s = 'First sentence. Second sentence.'
ss1 = s.split('e.')    #do a regular split
ss2 = re.split('e.',s) #do re.split
print(s)               #print sentence
#print split() results
print('s.split()')
for ss in ss1:
	print('\t"',ss,'"',sep='')
#print re.split() results
print('re.split()')
for ss in ss2:
	print('\t"',ss,'"',sep='')

