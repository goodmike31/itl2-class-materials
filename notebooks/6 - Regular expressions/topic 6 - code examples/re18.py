import re17

wordlist = re17.preprocess()
#sort the words
keys = sorted(wordlist.keys())
#print out the first 100 words
for i in range(100):
	print(keys[i],wordlist[keys[i]])
#print out the number of distinct words
print('Keys:',len(keys))

