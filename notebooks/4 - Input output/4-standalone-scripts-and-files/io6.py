import sys

vowels = 'aeiou'    #vowels
line = 1            #line number
#for each line in stdin
for words in sys.stdin:
	#print line number
	print('This is line',line)
	line += 1        #increment line count
	#break line into words
	for word in words.split():
		counter = 0   #continue as before
		vowelcount = 0
		while counter < len(word):
			if word[counter] in vowels:
				vowelcount += 1
			counter += 1
		else:
			print('\tThere are ',vowelcount,
				' vowels in "',word,'"',sep='')

