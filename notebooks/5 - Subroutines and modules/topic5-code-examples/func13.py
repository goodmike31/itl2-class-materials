x = [4,5,6]

def anotherfunc(a):
	a.append(7)
	return a

print(x)
print(anotherfunc(x))
print(x)

