import sys         #make sys.argv available

vowels = 'aeiou'   #define vowels
word = sys.argv[1] #get word from command-line
counter = 0        #proceed as before...
vowelcount = 0
while counter < len(word):
	if word[counter] in vowels:
		vowelcount += 1
	counter += 1
else:
	print('There are',vowelcount,
		'vowels in this word')

