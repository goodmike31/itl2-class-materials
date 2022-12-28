s = 'This is a sentence.'  #a test sentence
wds = s.split()            #split into words
hyphen = '-'               #define hyphen
#join bits with hyphen
hyphenated = hyphen.join(wds)
#print original sentence
print(s)
#print hyphenated sentence
print(hyphenated)

