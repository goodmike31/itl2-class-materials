import re

#define a string
s1 = 'This is a rather long string'
#replace '.s' with 'WOW'
s2 = re.sub('.s','WOW',s1)
#print old and new strings
print(s1,'\n',s2)

