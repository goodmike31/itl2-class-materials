#function to read in file
#and prune header info
def readfile(filename):
	f = open(filename,'r')
	text = f.read()
	f.close()
	text = text[10841:]
	return text

#invoke the function
t = readfile('alice.txt')
#print the number of letters
#to make sure this worked
print('characters:',len(t))

