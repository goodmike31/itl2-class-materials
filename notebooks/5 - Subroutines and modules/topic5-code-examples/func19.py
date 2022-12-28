def fac(n):     #function definition
	if n == 1:   #base case of recursion
		return 1
	else:        #recursive clause
		#invokes the function ITSELF
		return (n * fac(n-1))

#invoked with base case
print('1! =',fac(1))
#invoked with recursive case
print('5! =',fac(5))

