#open file
inFile = open('testfile.txt','r')
stuff = inFile.read()     #read file contents
inFile.close()            #close file
lines = stuff.split('\n') #split into lines
#print lines and lengths
for line in lines:
	print(len(line),': ',line,sep='')

