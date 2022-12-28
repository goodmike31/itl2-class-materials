import re

def preprocess():
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
	#split into words
	words = newtext.split()
	#eliminate single quotes
	newwords = []
	for w in words:
		word = ''
		for c in w:
			if c != "'":
				word += c
		newwords.append(word)
	#eliminate words with numbers
	finalwords = []
	for w in newwords:
		if re.search('[0-9]',w):
			continue
		else:
			finalwords.append(w)
	#do counts for words
	wordlist = {}
	for w in finalwords:
		if len(w) > 0:
			if w in wordlist:
				wordlist[w] += 1
			else:
				wordlist[w] = 1
	return wordlist

