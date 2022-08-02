import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()

position = input('Position - ')
repeat = input('Repeat - ')

# Retrieve all of the anchor tags

for i in range(int(repeat)):
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    lst = list()
    for tag in tags:
        lst.append(tag.get('href', None))
    html = urllib.request.urlopen(lst[int(position)-1], context=ctx).read()

print(re.findall('([A-Z][a-z]+)', lst[int(position)-1]))

# http://py4e-data.dr-chuck.net/known_by_Fikret.html
# http://py4e-data.dr-chuck.net/known_by_Avinash.html
