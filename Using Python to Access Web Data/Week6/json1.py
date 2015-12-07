import json
import urllib


#url = 'http://python-data.dr-chuck.net/comments_42.json'
url = 'http://python-data.dr-chuck.net/comments_195734.json'

data = urllib.urlopen(url) 
jsondata = data.read()
info = json.loads(str(jsondata))
print 'User count:', len(info)

sum = 0
print info
for item in info['comments']:
    print "Item:", item
    sum += item['count']

print "Final Sum:", sum
