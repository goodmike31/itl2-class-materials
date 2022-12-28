#import for timing your code
import time
#import for reading webpages
from urllib.request import urlopen

def mytime():   #return time in milliseconds
	return round(time.time() * 1000)

def myget(url): #read url and time that read
	start = mytime()
	data = urlopen(url,timeout=5).read()[:50]
	result = {"url": url, "data": data}
	now = str(mytime() - start)
	print(url + ": " + now + "ms")
	return result

#a random list of urls
urls = ['http://www.google.com/',
'http://www.yahoo.com/',
'http://golwg360.cymru/newyddion',
'https://news.google.com/news',
'https://tartarus.org/martin/PorterStemmer/',
'https://en.wikipedia.org/wiki/Main_Page',
'http://www.u.arizona.edu']

#start overall timing
start = mytime()
results = []    #list to collect results
#go through urls 1 by 1
for i in range(len(urls)):
	#get url and text read
	result = myget(urls[i])
	#append those to results
	results.append(result)
#get end time
now = str(mytime() - start)
#print overall time
print("Total = " + now + " ms\n")

