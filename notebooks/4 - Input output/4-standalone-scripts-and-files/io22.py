lines = []     #list for lines
#open file
f = open('alice.txt','r')
for line in f: #read lines one by one
	#add lines to list
	lines.append(line)
f.close()      #close file
#strip off first 255 lines
lines = lines[255:]
i = 0          #print first 50 lines
while i < 50:
	#still don't add a return!
	print(lines[i],end='')
	i += 1

