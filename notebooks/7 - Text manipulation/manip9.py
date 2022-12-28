import re,sys

#test if letter is consonant
#with respect to word!
def consonant(s,i):
	letter = s[i] #get relevant letter
	#it's not a consonant if it's aeiou
	if letter in 'aeiou':
		return False
	#word-initial y is a consonant
	elif letter == 'y' and i == 0:
		return True
	#it's a vowel if it follows a consonant
	elif letter == 'y' and consonant(s,i-1):
		return False
	else:         #otherwise it's a consonant
		return True

#stemming function frame again
def stem(w):
	return w

#get the command-line argument
word = sys.argv[1]
print(word)      #print it
#code to test the consonant() function
for i in range(len(word)):
	if consonant(word,i):
		print('C',end='')
	else:
		print('V',end='')
print()

