from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#most frequent Welsh words
welshwords = ['yn','y','i','a','o',
'ei','ar','yr','bod','ac',
'am','wedi','hi','ond','eu',
'fel','na','un','ni','mewn']

#function to test for Welsh
def welsh(u,t):
	n = t.lower()
	n = re.sub('[^a-z]',' ',n)
	n = re.sub('  +',' ',n)
	wds = n.split()
	total = len(wds)
	wcount = 0
	for w in wds:
		if w in welshwords:
			wcount += 1
	percent = wcount/total
	if percent > .08:
		return True
	else:
		return False

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
'https://cy.wikisource.org/wiki/Hafan',
'http://haciaith.com',
'http://techiaith.cymru',
'https://www.bbc.co.uk/cymru',
'https://www.yahoo.com',
'https://news.google.com/news/',
'https://en.wikipedia.org/wiki/Main_Page',
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
	t = s.get_text()
	#check if page is in Welsh
	if welsh(u,t):
		res.append([u,t])
		print(u,': ',len(t.split()),sep='')
print('Stored pages:',len(res))

