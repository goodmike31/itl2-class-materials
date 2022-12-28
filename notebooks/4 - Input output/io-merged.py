#not what we want!
x = 'Tom'
y = 'Dick'
z = 'Harry'

result = input('Type x, y, or z: ')

print(result)

#set up three variables
x = 'Tom'
y = 'Dick'
z = 'Harry'
#collect user input
result = input('Type x, y, or z: ')
#evaluate and print result
print(eval(result))

#open file stream
outFile = open('testfile.txt','w')
#write to it
outFile.write('some text!\n')
outFile.write('...and some more text!\n')
outFile.close()   #close file stream

#open file stream
inFile = open('testfile.txt','r')
stuff = inFile.read() #read form it
inFile.close()        #close stream
print(stuff)          #print contents

#open file
inFile = open('testfile.txt','r')
stuff = inFile.read()     #read file contents
inFile.close()            #close file
lines = stuff.split('\n') #split into lines
#print lines and lengths
for line in lines:
	print(len(line),': ',line,sep='')

#open file
inFile = open('testfile.txt','r')
#read from stream line by line
for line in inFile:
	#print length of line and the line
	print(len(line),': ',line,sep='',end='')
inFile.close()   #close file stream

#import from scipy and matplotlib
import scipy.io.wavfile,matplotlib.pyplot
#read sample rate and wave vector from file
x,y = scipy.io.wavfile.read('mha.wav')
vdur = len(y)/x            #calculate duration
#print duration
print('Duration of wave:',vdur)
matplotlib.pyplot.plot(y)  #make plot
matplotlib.pyplot.show()   #show plot

import openpyxl  #to handle xls/xlsx files

#read in data
wb = openpyxl.load_workbook('test.xlsx',
	read_only=True)

#get the names of 'sheets'
print(wb.get_sheet_names())
#get the first sheet
sheet = wb['Sheet1']
#print contents of cell B2 on sheet1
print(sheet['B2'].value)
r = 0            #keep track of rows
#go through all rows
for c in sheet.rows:
	print(r)      #print the row number
	#print cells in each row
	for i in range(len(c)):
		print('\t',c[i].value)
	r += 1

count = 0                 #counter for lines
f = open('alice.txt','r') #open the file
for line in f:            #read line by line
	count += 1
f.close()                 #close file
print('lines:',count)     #print line count

count = 0      #counter for lines
lines = []     #list for line contents
#open file
f = open('alice.txt','r')
for line in f: #read it line by line
	count += 1  #add 1 to counter
	#add current line to list
	lines.append(line)
f.close()      #close the file
#print number of lines read
print('lines:',count)
#print number of lines saved
print('saved lines:',len(lines))

import sys

print(sys.argv)

lines = []     #list to save lines
#open file
f = open('alice.txt','r')
for line in f: #read line by line
	#save each line in list
	lines.append(line)
f.close()      #close file
i = 0          #print first 100 lines
while i < 100:
	print(lines[i])
	i += 1

lines = []     #list to save lines
#open file
f = open('alice.txt','r')
for line in f: #read line by line
	#save lines to list
	lines.append(line)
f.close()      #close file
i = 0          #print first 100 lines
while i < 100:
	#don't add a return to the line!
	print(lines[i],end='')
	i += 1

lines = []     #list for lines
#open file
f = open('alice.txt','r')
for line in f: #read lines one by one
	#add lines to list
	lines.append(line)
f.close()      #close file
#strip off first 255 lines
lines = lines[255:]
i = 0          #print first 50 lines
while i < 50:
	#still don't add a return!
	print(lines[i],end='')
	i += 1

words = []     #list of all words
lines = []     #list of all lines

#open file
f = open('alice.txt','r')
for line in f: #save lines one by one
	lines.append(line)
f.close()      #close file

#remove Gutenberg header
lines = lines[255:]

#go through lines one by one
for line in lines:
	#break each line into words
	wds = line.split()
	#add words to list
	words += wds

i = 0 #print first 100 words
while i < 100:
	print(i,words[i])
	i += 1

words = []     #list of all words
lines = []     #list of all lines

#open file
f = open('alice.txt','r')
for line in f: #save lines one by one
	lines.append(line)
f.close()      #close file

#remove Gutenberg header
lines = lines[255:]

#go through lines one by one
for line in lines:
	wds = line.split()      #break into words
	words += wds            #add to list

#print first 100 words and letter counts
i = 0
while i < 100:
	#store the count for the current word
	count = 0
	#convert the current word to lowercase
	word = words[i].lower()
	#go through word letter by letter
	#if lowercase, add 1 to count
	for l in word:
		if l in "abcdefghijklmnopqrstuvwxyz":
			count += 1
	print(i,words[i],count) #print it all
	i += 1

words = []       #list of all words
lines = []       #list of all lines
wordlengths = {} #dictionary of word lengths

#open file
f = open('alice.txt','r')
for line in f:   #save lines one by one
	lines.append(line)
f.close()        #close file

#remove Gutenberg header
lines = lines[255:]

#go through the lines one by one
for line in lines:
	#break each line into words
	wds = line.split()
	#add the words to the list
	words += wds

for wd in words:
	count = 0     #count for current word
	#convert current word to lowercase
	word = wd.lower()
	#go through word letter by letter
	#if lowercase, add 1 to count
	for l in word:
		if l in "abcdefghijklmnopqrstuvwxyz":
			count += 1
	#check if we've seen this length before
	if count in wordlengths:
		#if so add 1
		wordlengths[count] += 1
	else:
		#if not, set to 1
		wordlengths[count] = 1

#print out counts for each word length
for c in wordlengths:
	print(c,wordlengths[c])

words = []       #list of all words
lines = []       #list of all lines
wordlengths = {} #dictionary of word lengths

#open file
f = open('alice.txt','r')
#save lines one by one
for line in f:
	lines.append(line)
f.close()        #close the file

#remove Gutenberg header
lines = lines[255:]

#go through lines one by one
for line in lines:
	#break each line into words
	wds = line.split()
	#add words to the list
	words += wds

for wd in words:
	count = 0     #count for current word
	#convert current word to lowercase
	word = wd.lower()
	#go through word letter by letter
	#if lowercase, add 1 to count
	for l in word:
		if l in "abcdefghijklmnopqrstuvwxyz":
			count += 1
	#check if we've seen this length already
	if count in wordlengths:
		#if so add 1
		wordlengths[count] += 1
	else:
		#if not, set to 1
		wordlengths[count] = 1

#open output file
g = open('res26.txt','w')
#print out counts for each word length
for c in wordlengths:
	clen = str(wordlengths[c])
	res = str(c) + ': ' + clen + '\n'
	g.write(res)
g.close()        #close output file

import sys         #make sys.argv available

vowels = 'aeiou'   #define vowels
word = sys.argv[1] #get word from command-line
counter = 0        #proceed as before...
vowelcount = 0
while counter < len(word):
	if word[counter] in vowels:
		vowelcount += 1
	counter += 1
else:
	print('There are',vowelcount,
		'vowels in this word')

import sys       #make sys.argv available

vowels = 'aeiou' #define vowels
#iterate over all words in list
for word in sys.argv[1:]:
	counter = 0   #proceed as before
	vowelcount = 0
	while counter < len(word):
		if word[counter] in vowels:
			vowelcount += 1
		counter += 1
	else:
		print('There are',vowelcount,
			'vowels in',word)

import sys

for line in sys.stdin:
	print(line)
import sys

vowels = 'aeiou'              #define vowels
#get each line in stdin
for words in sys.stdin:
	for word in words.split(): #break into words
		#do same as before to each
		counter = 0
		vowelcount = 0
		while counter < len(word):
			if word[counter] in vowels:
				vowelcount += 1
			counter += 1
		else:
			print('There are',vowelcount,
				'vowels in',word)

import sys

vowels = 'aeiou'    #vowels
line = 1            #line number
#for each line in stdin
for words in sys.stdin:
	#print line number
	print('This is line',line)
	line += 1        #increment line count
	#break line into words
	for word in words.split():
		counter = 0   #continue as before
		vowelcount = 0
		while counter < len(word):
			if word[counter] in vowels:
				vowelcount += 1
			counter += 1
		else:
			print('\tThere are ',vowelcount,
				' vowels in "',word,'"',sep='')

theInput = input('Type something: ')
print('You typed "',theInput,'"',sep='')

#collect two numbers
n1 = input('Enter a number: ')
n2 = input('Enter another number: ')
#convert to integers and add
n3 = int(n1) + int(n2)
print('The sum is:',n3)  #return result

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

