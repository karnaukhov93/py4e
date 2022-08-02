from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

lst = list()
tags = soup('span')
for tag in tags:
    x = re.findall('([0-9]+)', tag.decode())
    lst.append(int(x[0]))
print('Count', len(lst))
print('Sum', sum(lst))
