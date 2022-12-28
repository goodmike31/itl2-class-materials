#function that returns a function
def func(x):
	if x == 'L':
		return len
	else:
		return type

#invoking the function returns a
#function which we apply to
#'chair'. This may look confusing....
print(func('L')('chair'))

