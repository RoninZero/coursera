# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import re
import urllib
from BeautifulSoup import *

#url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Rishi.html'

html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
#tags = soup('a')
tags = soup('a')
print "TAGS", tags
for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   print 'URL:',tag.get('href', None)
   print 'Contents:',tag.contents[0]
   print 'Attrs:',tag.attrs

print "tags[2]:", tags[2]

print "Name:", url
for i in xrange(7):
   #print "Inner Name:", url
   html = urllib.urlopen(url).read()
   soup = BeautifulSoup(html)
   tags = soup('a')
   url = tags[17].get('href', None)
   print "Name:", url
