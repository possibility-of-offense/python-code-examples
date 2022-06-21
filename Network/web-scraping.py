import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter url - ')
html = urllib.request.urlopen(url).read()
parse_html = BeautifulSoup(html, 'html.parser')

heading = parse_html.find(string="The Second Page")
print(heading.parent)

anch = parse_html.find('a')
# print(anch.parent)

# tags = parse_html.find_all('a')
# for tag in tags :
#     print(tag.get('href', None))