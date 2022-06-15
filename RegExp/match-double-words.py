import re

m = re.match(r'(?P<letters>[abc]+)\w+\s+(?P=letters)', "abcda abc")
print(m)