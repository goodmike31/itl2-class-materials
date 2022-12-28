#module that can run on its own

myVar = 'hats and lemons'  #variable

def myFunc(s):             #function
	return len(s)

#if this is loaded on its own...
if __name__ == '__main__':
	print(myFunc(myVar))    #do this

