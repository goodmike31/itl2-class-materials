import urllib.request

#a url to read from
link = "http://www.u.arizona.edu/~hammond/"
#open a link to the url
f = urllib.request.urlopen(link)
#read the page
myfile = f.read()
#print the decoded page
print(myfile.decode('UTF-8'))

