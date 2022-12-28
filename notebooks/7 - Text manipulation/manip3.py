import re

#a test string
s1 = 'This is a rather long string'
#do a replacement
s2 = re.sub('t','WOW',s1)
#do a case-insensitive replacement
s3 = re.sub('t','WOW',s1,flags=re.I)
#incorporate case directly in the pattern
s4 = re.sub('t|T','WOW',s1)
#show all three results
print(s1,'\n',s2,'\n',s3,'\n',s4,sep='')

