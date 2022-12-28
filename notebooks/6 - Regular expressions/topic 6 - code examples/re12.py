f = open('alice.txt','r') #open file
text = f.read()           #read it all in
f.close()                 #close file stream
text = text[10841:]       #remove header
#convert to lowercase and split into words
words = text.lower().split()
#print first 50 words
for w in words[:50]:
	print(w)

