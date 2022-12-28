import random

letters = 'abcdefghijklmnopqrstuvwxyz'

#get random letter
letter = letters[random.randint(0,25)]

while True:              #loop until correct
	#prompt them to type a letter
	guess = input('Type a lower-case letter: ')
	#check that it's actually a letter
	if guess not in letters:
		print("That's not a lower-case letter.")
		continue
	if guess == letter:   #if they're right
		print("That's right!")
		break
	#give them a hint if they're wrong
	if guess > letter:
		print("It's earler in the alphabet.")
	else:
		print("It's later in the alphabet.")

