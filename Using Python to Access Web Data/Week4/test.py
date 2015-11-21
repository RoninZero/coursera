#!/usr/bin/python3

import re

# string for which to test
#str = "From: none@nowhere.none.net Sun Nov  2 20:01:15 2015"

str = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'

# example regex
#found = re.findall('^From: (\S+@\S+)', str)
found = re.findall('href="(.+)"', str)

print(found)



