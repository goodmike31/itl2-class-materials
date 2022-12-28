#open a file to read bytes
f = open('enc/cb5.txt','rb')
c = f.read()          #read the bytes
#convert from big5 to utf8 characters
c = c.decode('big5')
print('Chinese:',c)   #print characters

#open a file to read bytes
f = open('enc/r1251.txt','rb')
r = f.read()          #read the bytes
#convdert from windows-1251 to utf8
r = r.decode('1251')
print('Russian:',r)   #print characters

