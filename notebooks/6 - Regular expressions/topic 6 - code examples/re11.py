f = open('alice.txt','r') #open the file
text = f.read()           #read it all in
f.close()                 #close file stream
#print first 100 letters to make sure
print(text[:100])

