import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('https://data.pr4e.org/cover.jpg')
fhand = open('new-image.jpg', 'wb')

while True :
    data = img.read(100000)
    if len(data) < 1 :
        break

    fhand.write(data)

fhand.close()