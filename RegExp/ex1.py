import re

# Match word starting with X- followed by any characters (zero or more times), then ending with :
# my_str_pre = 'X-Plane:'
# re1 = re.search('^X.*:', my_str)

# Match word starting with X- followed by word with upper and lower cases letters, which has
# zero or more whitespaces followed by :
# my_str_pre = 'X-Plane is behing schedule: two weeks'
# re2 = re.search('^X-[A-Za-z]+\s*:', my_str_pre)

# Find email domain
# email = 'blah.blah@uct.az.za'
# re3 = re.findall('\S+@(\S+)',email)
# everything that has @ and non-blank characters after that
# re3 = re.findall('@([^ ]*)', email)

# Find the numbers following this format X-DSPAM-Confidence: 0.8475
# f_handle = open('../mailbox.txt')
# empty_list = list()

# for line in f_handle :
#     line = line.rstrip()

#     reg = re.search('^X-[A-Z]+-[A-Z][a-z]+: ([0-9].*[0-9]*)', line)
    
#     if reg != None :
#         empty_list.extend(re.findall('^X-[A-Z]+-[A-Z][a-z]+: (\d+.\d+)', line))

# print(float(max(empty_list)))

my_str = 'X-Something:'
re4 = re.search('[A-Z]', my_str)
print(re4)

