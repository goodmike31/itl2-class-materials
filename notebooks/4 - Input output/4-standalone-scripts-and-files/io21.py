lines = []     #list to save lines
#open file
f = open('alice.txt','r')
for line in f: #read line by line
	#save lines to list
	lines.append(line)
f.close()      #close file
i = 0          #print first 100 lines
while i < 100:
	#don't add a return to the line!
	print(lines[i],end='')
	i += 1

