import re

#open local page
f = open('hammond.html','r')
t = f.read()     #read it all in
f.close()        #close file stream
#eliminate header up to body of page
t = re.sub('^.*<body>','',t,flags=re.I|re.S)
#remove all tags
t = re.sub('<[^>]*>',' ',t,flags=re.I|re.S)
print(t)         #print what's left

