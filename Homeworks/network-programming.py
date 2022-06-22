# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')

last_name = ''
parse = re.search('known_by_(\w+).html', url)
last_name = parse.group(1)

count = int(input('Enter count: '))
position = int(input('Enter position: '))
html = urllib.request.urlopen(url, context=ctx).read()
anchor = ''

for i in range(count) :
    soup = BeautifulSoup(html, 'html.parser')

    tag = soup.find('ul')
    
    for ind, child in enumerate(tag.find_all('li')) :
        if ind + 1 == position :
            anchor = child.contents
            parse = re.search('known_by_(\w+).html', anchor[0].get('href'))
            last_name = parse.group(1)
            html = urllib.request.urlopen(anchor[0].get('href'), context=ctx).read()

    
print(last_name)