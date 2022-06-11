file_handle = open('mail-example.txt')
collect_senders = list()
count_senders = 0

for line in file_handle :
    remove_new_lines = line.rstrip()
    split_str = remove_new_lines.split(' ')

    if not line.startswith('From:') : continue
    else : count_senders += 1

    for ind, word in enumerate(split_str) :
        if ind > 0 :
            get_name = word.split('@')[0].replace('.', ' ').capitalize()

            if get_name in collect_senders :
                continue
            else :
                collect_senders.append(get_name)
            

print(collect_senders)
print(f'There were {count_senders} lines in the file with From as the first word')