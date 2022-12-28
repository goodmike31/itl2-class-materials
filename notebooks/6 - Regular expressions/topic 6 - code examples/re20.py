import re,re17

#get the word counts
wordlist = re17.preprocess()
words = wordlist.keys()  #just get the words
clusters = []            #strip off onsets
for w in words:
	m = re.search('^([^aeiouy]*)[aeiouy]',w)
	if m:
		if m.end(1) == 0 and w[0] == 'y':
			onset = 'y'
		else:
			onset = w[0:m.end(1)]
		clusters.append(onset)
#eliminate duplicate onsets
clusters = sorted(set(clusters))
for c in clusters:       #print all onsets
	print("'",c,"'",sep='')
#print number of onsets
print(len(clusters))

