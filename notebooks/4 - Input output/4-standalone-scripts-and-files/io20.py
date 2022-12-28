lines = []     #list to save lines
#open file
f = open('alice.txt','r')
for line in f: #read line by line
	#save each line in list
	lines.append(line)
f.close()      #close file
i = 0          #print first 100 lines
while i < 100:
	print(lines[i])
	i += 1

