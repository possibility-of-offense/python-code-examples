import re

# some_date = 'My date is this formated 28/02/1990 blah'
# find_1 = re.findall('\d{2}/\d{2}/\d{4}', some_date)

# def format_date(d) :
#     for single_d in d :
#         new_d = single_d.split('/')
#         print(f'The day was {new_d[0]}, the month was {new_d[1]} and the year was {new_d[2]}!')


# format_date(find_1)

# str_1 = 'Some chars \n what \n the f'
# remove_new_lines = list(map(lambda x : x.replace('\n', ''), re.findall('.*the', str_1, re.DOTALL)))
# print(remove_new_lines)

print(re.findall('a[bcd]*b', 'abcbd'))