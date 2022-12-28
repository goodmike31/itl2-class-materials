def myfunc():         #a function
	#user supplies a word
	word = input('Word: ')
	#print that word
	print('This is your word:',word)
	if len(word) > 5:  #check if > 5
		print('Your word was long.')
	else:
		print('Your word was short.')

myfunc()              #invoke function

