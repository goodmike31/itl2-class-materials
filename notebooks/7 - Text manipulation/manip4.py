#make a translation table
mytab = str.maketrans('aeiou','happy')
#a test string
s = 'This is my sample string'
print(s)                  #print that string
print(s.translate(mytab)) #print translation

