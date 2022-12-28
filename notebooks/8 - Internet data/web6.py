import re

#open local file
f = open('hammond.html','r')
t = f.read()     #read whole thing in
f.close()        #close the stream
#do a multi-line substitution, deleting
#everything up to the body of the page
t = re.sub('^.*<body>','',t,flags=re.I|re.S)
print(t)         #print the result

