import re,re17

#get the word counts
wordlist = re17.preprocess()
#just get the words
words = wordlist.keys()
clusters = []        #strip off onsets
for w in words:
	m = re.search('^[^aeiou]*',w)
	if m:
		onset = w[0:m.end()]
		clusters.append(onset)
#eliminate duplicate onsets
clusters = sorted(set(clusters))
for c in clusters:   #print all onsets
	print("'",c,"'",sep='')
print(len(clusters)) #print number of onsets

