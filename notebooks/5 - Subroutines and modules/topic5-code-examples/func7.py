word = input('Word: ') #user supplies word

#function refers to previous value!
def myfunc():
	print('This is your word:',word)

myfunc()               #invoke function
#check if word is less than 5 letters
if len(word) < 5:
	print("Your word wasn't long enough")

