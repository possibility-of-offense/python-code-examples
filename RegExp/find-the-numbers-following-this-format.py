import re

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

