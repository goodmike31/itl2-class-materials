#a function to print that sentence
def myfunc():
	print('Colorless green ideas...')
	print('...sleep furiously')

myfunc()    #invoke the function
#collect the number
num = input('Enter a number: ')
#check if the number is < 5
if int(num) < 5:
	myfunc() #print sentence again if so
else:
	print('Your number was big enough')

