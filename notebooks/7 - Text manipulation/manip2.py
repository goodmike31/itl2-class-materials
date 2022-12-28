import re

#a test string
s1 = 'This is a rather long string'
pat = '.s'     #a pattern
#find how many instances of the pattern
countmax = len(re.findall(pat,s1))
print(s1)      #print the string
i = 1          #make substitutions 1 by 1
while i < countmax+1:
	#make a change
	s2 = re.sub(pat,'WOW',s1,count=i)
	#print that one change
	print('\t',i,':',s2)
	i += 1      #increment counter

