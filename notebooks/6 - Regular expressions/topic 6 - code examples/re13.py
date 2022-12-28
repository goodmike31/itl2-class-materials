import re

f = open('alice.txt','r')  #read in Alice
text = f.read()
f.close()
text = text[10841:]        #strip header
#convert to lower case
lowertext = text.lower()
#punctuation to convert
punc = '[\.\?\-!\?\*,"\(\):\`\[\];_/~]'
#convert punctuation to space
newtext = ''
for c in lowertext:
	if re.search(punc,c):
		newtext += ' '
	else:
		newtext += c
words = newtext.split()    #split into words
#print first 50 words
for w in words[:50]:
	print(w)

