r = 'русский язык'   #a string in Russian
#open a connection to write bytes
f = open('enc/rout1251.txt','wb')
#write bytes in windows-1251
f.write(r.encode('1251'))
f.close()            #close connection
#a string in chinese
c = '中文'
#open a connection to write bytes
f = open('enc/coutb5.txt','wb')
#write bytes in big5
f.write(c.encode('big5'))
f.close()            #close connection

