import urllib.request, urllib.parse, urllib.error

data = ''
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand :
    data += line.decode().strip() + '\n'

f_handle = open('sample-text.txt', 'w')
f_handle.write(data)