words = []     #list of all words
lines = []     #list of all lines

#open file
f = open('alice.txt','r')
for line in f: #save lines one by one
	lines.append(line)
f.close()      #close file

#remove Gutenberg header
lines = lines[255:]

#go through lines one by one
for line in lines:
	wds = line.split()      #break into words
	words += wds            #add to list

#print first 100 words and letter counts
i = 0
while i < 100:
	#store the count for the current word
	count = 0
	#convert the current word to lowercase
	word = words[i].lower()
	#go through word letter by letter
	#if lowercase, add 1 to count
	for l in word:
		if l in "abcdefghijklmnopqrstuvwxyz":
			count += 1
	print(i,words[i],count) #print it all
	i += 1

