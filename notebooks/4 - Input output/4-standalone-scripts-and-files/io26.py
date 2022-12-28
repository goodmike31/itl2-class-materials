words = []       #list of all words
lines = []       #list of all lines
wordlengths = {} #dictionary of word lengths

#open file
f = open('alice.txt','r')
#save lines one by one
for line in f:
	lines.append(line)
f.close()        #close the file

#remove Gutenberg header
lines = lines[255:]

#go through lines one by one
for line in lines:
	#break each line into words
	wds = line.split()
	#add words to the list
	words += wds

for wd in words:
	count = 0     #count for current word
	#convert current word to lowercase
	word = wd.lower()
	#go through word letter by letter
	#if lowercase, add 1 to count
	for l in word:
		if l in "abcdefghijklmnopqrstuvwxyz":
			count += 1
	#check if we've seen this length already
	if count in wordlengths:
		#if so add 1
		wordlengths[count] += 1
	else:
		#if not, set to 1
		wordlengths[count] = 1

#open output file
g = open('res26.txt','w')
#print out counts for each word length
for c in wordlengths:
	clen = str(wordlengths[c])
	res = str(c) + ': ' + clen + '\n'
	g.write(res)
g.close()        #close output file

