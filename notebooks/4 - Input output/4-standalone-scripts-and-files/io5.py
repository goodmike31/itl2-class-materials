import sys

vowels = 'aeiou'              #define vowels
#get each line in stdin
for words in sys.stdin:
	for word in words.split(): #break into words
		#do same as before to each
		counter = 0
		vowelcount = 0
		while counter < len(word):
			if word[counter] in vowels:
				vowelcount += 1
			counter += 1
		else:
			print('There are',vowelcount,
				'vowels in',word)

