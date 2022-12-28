#import for reading urls
import urllib.request
#import for parsing html
from bs4 import BeautifulSoup

#non-local page this time
link = "http://www.u.arizona.edu/~hammond/"
#connect to that page
f = urllib.request.urlopen(link)
myfile = f.read()       #read it all in
#build a document model
soup = BeautifulSoup(myfile,'html.parser')
print(myfile)           #print page verbatim
print(soup.prettify())  #pretty-print html
print(soup.get_text())  #extract the text
#got through all the hyperlinks...
for link in soup.find_all('a'):
	#...and print them
	print(link.get('href'))

