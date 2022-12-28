from urllib.request import urlopen

#seed for list of urls
urls = ['http://golwg360.cymru',
'http://www.u.arizona.edu/~hammond']
res = []            #results
i = 1               #iterate through list
while urls and i < 100:
	u = urls.pop(0)  #open/read url
	w = urlopen(u,timeout=5)
	t = w.read()
	#placeholder: count words
	print(i,': ',len(t.split()),sep='')
	i += 1
	#check if page is in Welsh
	if True:
		res.append([u,t])
		#extract links and append

