import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url)<1 :
    quit()
else:
    u = urllib.request.urlopen(url, context=ctx)
    print('Retrieving', url)
    data = u.read()
    print('Retrieved', len(data.decode()), 'characters')

    lst=list()
    info = json.loads(data)
    for item in info.get('comments'):
        lst.append(item['count'])
    print('Count:', len(lst))
    print('Sum:', sum(lst))

#http://py4e-data.dr-chuck.net/comments_42.json
#http://py4e-data.dr-chuck.net/comments_1449228.json
