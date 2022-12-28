#function with default for 2nd arg
def f(x,y='oops'):
	return x + ' ' + y

print(f('hat'))     #invoked 3 ways
print(f(x='chair'))
print(f('hat','chair'))

