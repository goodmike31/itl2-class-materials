from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#fix relative and local links
def fixlinks(u,l):
	res = re.sub('#.*$','',l)
	m = re.search('^http',res)
	if m:
		return res
	res = u + '/' + res
	res = re.sub('([^:]/)/+','\\1',res)
	return res

#seed for list of urls
urls = ['http://golwg360.cymru',
'http://bad',
'http://www.u.arizona.edu/~hammond/greeting.au',
'http://www.u.arizona.edu/~hammond']
res = []               #results
i = 1                  #iterate through list
while urls and i < 100:
	u = urls.pop(0)     #open/read url
	i += 1
	try:
		w = urlopen(u,timeout=5)
		h = w.read()
		h = h.decode('UTF-8')
	except:
		print('bad url:',u)
		continue
	#parse html
	s = BeautifulSoup(h,'html.parser')
	t = s.body.get_text()
	#check if the page is in Welsh
	if True:
		res.append([u,t])
		print(u,': ',len(t.split()),sep='')
print('Stored pages:',len(res))

