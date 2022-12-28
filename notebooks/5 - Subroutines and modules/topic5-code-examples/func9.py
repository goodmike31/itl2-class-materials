def sillyfunc():    #function definition
	#user supplies a word
	wd = input('Type a word: ')
	if len(wd) > 4:  #check length of word
		#return length and exit function
		return len(wd)
	else:            #otherwise...
		print('The word is too short!')

res = sillyfunc()   #save value of function
#print value of variable
print('The result: ',res)

