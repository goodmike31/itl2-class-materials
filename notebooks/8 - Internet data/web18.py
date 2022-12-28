from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#seed for list of urls
urls = ['http://golwg360.cymru',
'http://www.u.arizona.edu/~hammond']
res = []               #results
i = 1                  #iterate through list
while urls and i < 100:
	u = urls.pop(0)     #open/read url
	w = urlopen(u,timeout=5)
	h = w.read()
	#parse html
	s = BeautifulSoup(h,'html.parser')
	t = s.body.get_text()
	i += 1
	#check if page is in Welsh
	if True:
		res.append([u,t])
		print(u,': ',len(t.split()),sep='')
		#extract links
		links = s.find_all('a')
		for l in links:
			print('\t',l.get('href'))

