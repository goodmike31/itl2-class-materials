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
	#break each line into words
	wds = line.split()
	#add words to list
	words += wds

i = 0 #print first 100 words
while i < 100:
	print(i,words[i])
	i += 1

