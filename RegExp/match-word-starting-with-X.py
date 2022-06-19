import re

# Match word starting with X- followed by any characters (zero or more times), then ending with :
# my_str_pre = 'X-Plane:'
# re1 = re.search('^X.*:', my_str)

# Match word starting with X- followed by word with upper and lower cases letters, which has
# zero or more whitespaces followed by :
# my_str_pre = 'X-Plane is behing schedule: two weeks'
# re2 = re.search('^X-[A-Za-z]+\s*:', my_str_pre)
