count = 0      #counter for lines
lines = []     #list for line contents
#open file
f = open('alice.txt','r')
for line in f: #read it line by line
	count += 1  #add 1 to counter
	#add current line to list
	lines.append(line)
f.close()      #close the file
#print number of lines read
print('lines:',count)
#print number of lines saved
print('saved lines:',len(lines))

