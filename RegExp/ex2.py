# Some of our email addresses have incorrect characters like “<” or “;” at the beginning or end. Let’s declare that we are only interested in the portion of the string that starts and ends with a letter or a number.
# To do this, we use another feature of regular expressions. Square brackets are used to indicate a set of multiple acceptable characters we are willing to consider matching. In a sense, the \S is asking to match the set of “non-whitespace characters”. Now we will be a little more explicit in terms of the characters we will match.
# Here is our new regular expression:

# Notice that on the source@collab.sakaiproject.org lines, our regular expression eliminated 
# two letters at the end of the string (“>;”). This is because when we append [a-zA-Z] to the end of our 
# regular expression, we are demanding that whatever string the regular expression parser finds must end with a 
# letter. So when it sees the “>” at the end of “sakaiproject.org>;” 
# it simply stops at the last “matching” letter it found (i.e., the “g” was the last good match).

# ^X-.*: [0-9.]+

# Translating this, we are saying, we want lines that start with X-, followed by zero or more characters (.*), 
# followed by a colon (:) and then a space. After the space we are looking for one or more characters 
# that are either a digit (0-9) or a period [0-9.]+. Note that inside the square brackets, 
# the period matches an actual period (i.e., it is not a wildcard between the square brackets).

# [a-zA-Z0-9]\S*@\S*[a-zA-Z]

import re

# Extract all revision numbers

# rev_str = 'Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772'
# reg_pattern = '^[A-Z][a-z]+: http:\S+&rev=(\d+)'

# re1 = re.findall(reg_pattern, rev_str)
# # print(re1)

# # Get time of day
# time_of_day = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# reg_pattern2 = '^From .+ (\d+:\d+:\d+)'

# re2 = re.findall(reg_pattern2, time_of_day)
# print(re2)

# Word boundaries or in the case of \B not word boundaries :D

# my_str2 = 'dafooda'
# print(re.findall(r'\BFoo\B', my_str2, re.I))
# my_str2 = 'da foo da'
# print(re.findall(r'\bfoo\b', my_str2))

file_handle = open('../mailbox.txt')
gather_numbers = list()

for line in file_handle :
    line = line.rstrip()

    reg_pattern = '.* [rR]evision: (\d+|\d+.\d+)'
    gather_numbers.extend(re.findall(reg_pattern, line))

gather_numbers = list(map(lambda x : int(x), gather_numbers))

print(int(sum(gather_numbers) / len(gather_numbers)))