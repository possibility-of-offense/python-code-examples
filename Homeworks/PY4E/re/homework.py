import re
file_handle = open('actual-data.txt')
all_nums = list()

for line in file_handle :
    line = line.rstrip()
    reg_pattern = '\d+'

    nums = re.findall(reg_pattern, line)
    all_nums.extend(nums)

all_nums_parsed = list(map(lambda x : int(x), all_nums))

# print(sum(all_nums_parsed))

# print(file_handle.read())
print(sum([int(numb) for numb in re.findall('[0-9]+', open('actual-data.txt').read())]))
