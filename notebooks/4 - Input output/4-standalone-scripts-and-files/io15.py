#open file
inFile = open('testfile.txt','r')
#read from stream line by line
for line in inFile:
	#print length of line and the line
	print(len(line),': ',line,sep='',end='')
inFile.close()   #close file stream

