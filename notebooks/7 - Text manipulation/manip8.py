import re,sys

#stemming function for words in -ed
def stem(w):
	#does the word end in ed?
	m = re.search('(^.*)ed$',w)
	if m:                 #if it does...
		return m.group(1)  #return the stem
	else:                 #if it doesn't...
		return w           #just return word

#get word from command-line
word = sys.argv[1]
root = stem(word)        #stem it
#print word and stem
print(word,':\t',root,sep='')

