import sys

def stem(w):        #stemming function frame
	return w

#get word from command-line
word = sys.argv[1]
root = stem(word)   #stem it!
#print word and its stem
print(word,':\t',root,sep='')

