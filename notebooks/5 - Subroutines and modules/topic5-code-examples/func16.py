#function with unspecified
#number of unnamed and named arguments
def func(*args,**kwargs):
	for a in args:   #print unnamed args
		print(a)
	for k in kwargs: #print named args
		print(k,'\t',kwargs[k])

#invoked with unnamed FOLLOWED by
#named arguments
func(3,6,8,hat='wow',chair=3.5)

