import time      #for timing info
#to read webpages
from urllib.request import urlopen
#to do more than one thing at once
from multiprocessing import Pool

#current time in milliseconds
def mytime():
	return round(time.time() * 1000)

def myget(url):  #50 characters of a webpage
	start = mytime()
	data = urlopen(url,timeout=5).read()[:50]
	result = {"url": url, "data": data}
	now = str(mytime() - start)
	print(url + ": " + now + "ms")
	return result

#some random urls
urls = ['http://www.google.com/',
'http://www.yahoo.com/',
'http://golwg360.cymru/newyddion',
'https://news.google.com/news',
'https://tartarus.org/martin/PorterStemmer/',
'https://en.wikipedia.org/wiki/Main_Page',
'http://www.u.arizona.edu']

#print urls in order accessed
for i in range(len(urls)):
	print(i+1,': ',urls[i],sep='')
print()

mypool = Pool()  #multiple processes
start = mytime() #start the clock
#separate process for each url
results = mypool.map(myget, urls)
#print total elapsed
now = str(mytime() - start)
print("Total = " + now + " ms\n")

