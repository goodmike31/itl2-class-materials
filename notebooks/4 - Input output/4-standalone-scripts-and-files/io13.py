#open file stream
inFile = open('testfile.txt','r')
stuff = inFile.read() #read form it
inFile.close()        #close stream
print(stuff)          #print contents

