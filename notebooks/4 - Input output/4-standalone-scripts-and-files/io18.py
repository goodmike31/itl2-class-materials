count = 0                 #counter for lines
f = open('alice.txt','r') #open the file
for line in f:            #read line by line
	count += 1
f.close()                 #close file
print('lines:',count)     #print line count

