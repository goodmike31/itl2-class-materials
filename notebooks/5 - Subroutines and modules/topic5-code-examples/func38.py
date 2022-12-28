f = open('alice.txt','r') #open file
text = f.read()           #read whole text
f.close()                 #close file stream
print(text[:10840])       #print the header
text = text[10841:]       #remove the header
#something to separate two print statements
print('NEW START OF FILE:\n')
#print first 100 letters of what remains
print(text[:100])

