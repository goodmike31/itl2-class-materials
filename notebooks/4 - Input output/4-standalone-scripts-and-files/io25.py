words = []       #list of all words
lines = []       #list of all lines
wordlengths = {} #dictionary of word lengths

#open file
f = open('alice.txt','r')
for line in f:   #save lines one by one
	lines.append(line)
f.close()        #close file

#remove Gutenberg header
lines = lines[255:]

#go through the lines one by one
for line in lines:
	#break each line into words
	wds = line.split()
	#add the words to the list
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
	#check if we've seen this length before
	if count in wordlengths:
		#if so add 1
		wordlengths[count] += 1
	else:
		#if not, set to 1
		wordlengths[count] = 1

#print out counts for each word length
for c in wordlengths:
	print(c,wordlengths[c])

