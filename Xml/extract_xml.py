import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

list_1=list()
url = input('Enter location: ')
if len(url) < 1:
    quit()
else:
    print('Retrieving', url)
    u = urllib.request.urlopen(url, context=ctx)
    data = u.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)
    lst = tree.findall('comments/comment')
    for item in lst:
        list_1.append(int(item.find('count').text))
print('Count:', len(list_1))
print('Sum:', sum(list_1))

#http://py4e-data.dr-chuck.net/comments_42.xml
#http://py4e-data.dr-chuck.net/comments_1449227.xml
