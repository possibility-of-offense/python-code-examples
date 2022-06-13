file_handle = open('words.txt', 'r+', encoding="utf-8")
words = list()

for (num_line, line) in enumerate(file_handle) :
    if num_line % 2 == 0 : continue
    else :
        trim_line = line.rstrip()
        split_line = trim_line.split(' ')

        for word in split_line:
            words.append((len(word), word))

words.sort(reverse = True)

file_handle.write(f'\nThe biggest word is {words[0][1]}!')
file_handle.close()