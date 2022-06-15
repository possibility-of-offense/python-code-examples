import re

some_str = 'Paris in the the spring aha aha'

p = re.compile(r'\b(\w+)\s+\1')
to_replace = p.findall(some_str)

for val in to_replace :
    some_str = some_str.replace(val, '').replace('  ','')

print(some_str)