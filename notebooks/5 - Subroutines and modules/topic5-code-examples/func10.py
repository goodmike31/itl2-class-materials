def myfunc():      #function definition
	#collect two strings
	x = input('First string: ')
	y = input('Second string: ')
	z = x + ' ' + y #concatenate strings
	#return all three
	return len(x),len(y),z

#invoke function saving all
a,b,c = myfunc()   #3 return values
print('a =',a)     #print the 3 values
print('b =',b)
print('c =',c)

