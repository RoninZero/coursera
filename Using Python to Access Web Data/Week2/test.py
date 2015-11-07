#!/usr/bin/python3

import re

# string for which to test
str = "From: none@nowhere.none.net Sun Nov  2 20:01:15 2015"

# example regex
found = re.findall('^From: (\S+@\S+)', str)

print(found)

'''
Question 1
'''
str1 = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
found1 =  re.findall('@(\S+)', str1)
print("Question 1:")
print(found1)

'''
Question 8
'''
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print("Question 8:")
print(y)

'''
Question 10
'''
str10 = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
found10 =  re.findall('\S+?@\S+', str1)
print("Question 10:")
print(found10)


