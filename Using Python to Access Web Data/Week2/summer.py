#!/usr/bin/python3

import re
from sys import argv

script, filename = argv

txt = open(filename)

testing = [ '1', '2', '3', '4' ]

newsum = 0

for val in testing:
    newsum += int(val)
print("Sum:", newsum) 
