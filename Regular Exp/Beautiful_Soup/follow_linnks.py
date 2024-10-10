# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
cnt=int(input('Enter count:'))
pos=int(input('Enter Position:'))
ps=0
# Retrieve all of the anchor tags

for i in range(0+1, cnt+1):
    # print(i,'range!!')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags =soup('a')
    for tag in tags:
        ps=ps+1
        # print(tag)
        if ps==pos:
            print('Retrieving:', tag.get('href', None))
            url=tag.get('href', None)
            ps=0
            break