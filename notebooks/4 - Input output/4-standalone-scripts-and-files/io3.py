import sys       #make sys.argv available

vowels = 'aeiou' #define vowels
#iterate over all words in list
for word in sys.argv[1:]:
	counter = 0   #proceed as before
	vowelcount = 0
	while counter < len(word):
		if word[counter] in vowels:
			vowelcount += 1
		counter += 1
	else:
		print('There are',vowelcount,
			'vowels in',word)

