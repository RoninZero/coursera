#!/usr/bin/python3

import re

# string for which to test
str = "From: none@nowhere.none.net Sun Nov  2 20:01:15 2015"

# example regex
found = re.findall('^From: (\S+@\S+)', str)

print(found)
