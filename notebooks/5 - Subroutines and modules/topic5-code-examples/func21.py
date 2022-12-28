def makeAddN(n):   #function definition
	#returns new function
	return lambda x: x + n

#invoke twice, making 2 new functions
add2 = makeAddN(2)
add6 = makeAddN(6)
#apply those two new functions
print(add2(17))
print(add6(17))

