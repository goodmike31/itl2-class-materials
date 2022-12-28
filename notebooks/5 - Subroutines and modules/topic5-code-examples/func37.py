f = open('alice.txt','r') #open file
text = f.read()           #read it all in
f.close()                 #close stream
#check that that worked!
print('characters:',len(text))

