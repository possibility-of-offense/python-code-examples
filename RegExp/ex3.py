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

# print(re.findall('a[bcd]*b', 'abcbd'))

# my_str = r'\nection'
# prog = re.compile(my_str)

# str_to_check = '\\nection is blah \\nection'
# print(re.finditer(r'\\nection', str_to_check))

# stackoverflow
# https://stackoverflow.com/questions/33582162/confused-about-backslashes-in-regular-expressions

# An alternate way to have search() consider '\' as a character is to place an r before the regular expression. 
# This tells the Python interpreter to NOT preprocess the string.

# p = re.compile(r'test\s([a-z]+)')
# test_str = 'test dada blah blah'

# m = p.finditer(test_str)

# for match in m :
#     print(match.group())

# backreference

# m = re.match("(?:[abc])+", "abc")
# print(m.groups())

# my_str = 'Ventsi 123 what 123 test 123'

# new_s = re.split(r'\d{3}', my_str)
# print(new_s)

# p = re.compile('x')
# new_p = p.sub('-', 'abxxxd')
# print(new_p)

init_str = 'My name is blah Ventsislav'
# mapping = init_str.maketrans('blah', 'nqay')

# init_str = init_str.replace('blah', '')
init_str = re.sub('\sblah', '', init_str)
print(init_str)