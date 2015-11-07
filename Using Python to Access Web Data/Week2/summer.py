#!/usr/bin/env python3

import re
from sys import argv

script, filename = argv

txt = open(filename)

values = re.findall('[0-9]+', txt.read())
#print("Text:", txt.read())
print("Values:", values)

testing = [ '1', '2', '3', '4' ]
newsum = 0
for val in values:
    newsum += int(val)
print("Sum:", newsum) 
