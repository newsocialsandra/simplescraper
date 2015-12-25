import urllib
from BeautifulSoup import *

url = raw_input('Enter URL:')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')

count = 0
summ = 0
for t in tags:
	summ += int(t.contents[0])
	count += 1

print 'Count:', count
print 'Sum:', summ