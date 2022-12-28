f = open('enc/russian.txt','r')
r = f.read()
f.close()
print('Some Russian:',r,end='')

f = open('enc/chinese.txt','r')
c = f.read()
f.close()
print('Some Chinese:',c,end='')
