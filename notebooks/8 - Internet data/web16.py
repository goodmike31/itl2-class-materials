from urllib.request import urlopen

#welsh news site
url = 'http://golwg360.cymru'
w = urlopen(url,timeout=5)  #open connection
t = w.read()                #read whole page
#print number of words
print(len(t.split()))

