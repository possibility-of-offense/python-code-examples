import xml.etree.ElementTree as ET

data = '''<person>
 <devs>
    <dev>Dev 1</dev>
    <dev>Dev 2</dev>
    <dev>Dev 3</dev>
 </devs>
</person>'''

tree = ET.fromstring(data)

devs = tree.findall('devs/dev')

for dev in devs:
    print(dev.text)