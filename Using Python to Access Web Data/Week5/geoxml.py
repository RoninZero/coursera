import urllib
import xml.etree.ElementTree as ET

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
#url = 'http://python-data.dr-chuck.net/comments_42.xml'
url = 'http://python-data.dr-chuck.net/comments_195730.xml'

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
print data
tree = ET.fromstring(data)


results = tree.findall('.//count')
print "Count:", len(results)
sum = 0
for result in results:
    print "Result:", result.text
    sum += int(result.text)

print "Sum:", sum
