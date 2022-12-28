print('Before the first try block:')
try:
	print('\tthree' + 3)
except:
	print("\tThat math doesn't work.")
print('Before the second try block:')
try:
	print('\tthree' + ' + 3.')
except:
	print("That math doesn't work.")
print('All done.')

