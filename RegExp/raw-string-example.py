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