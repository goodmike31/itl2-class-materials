import re,re17

#get the word counts
wordlist = re17.preprocess()
#just get the words
words = wordlist.keys()
#strip off onsets and do counts
clusters = {}
for w in words:
	m = re.search('^([^aeiouy]*)[aeiouy]',w)
	if m:
		if m.end(1) == 0 and w[0] == 'y':
			ons = 'y'
		else:
			ons = w[0:m.end(1)]
		if ons in clusters:
			clusters[ons] += 1
		else:
			clusters[ons] = 1
#print onset counts
keys = sorted(clusters.keys())
for c in keys:
	print("'",c,"': ",clusters[c],sep='')

