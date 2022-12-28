import sys,re
#read in 'Alice' and break into words
f = open('alice.txt','r')
words = f.read().split()
f.close()
for w in words:  #match against each word
	m = re.search(sys.argv[1],w)
	if m:
		print(w)

