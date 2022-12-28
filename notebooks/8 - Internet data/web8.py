import re

#open local webpage
f = open('hammond.html','r')
t = f.read()     #read it all in
f.close()        #close file stream
#get rid of header
t = re.sub('^.*<body>','',t,flags=re.I|re.S)
#get rid of (at least some) html comments
t = re.sub(
	'<!--[^-]*-->',' ',t,flags=re.I|re.S
)
#get rid of at least some tags
t = re.sub('<[^>]*>',' ',t,flags=re.I|re.S)
print(t)          #print what remains

