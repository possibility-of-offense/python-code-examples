try :
    file_handle = open('../mailbox.txt')
except :
    print('The file is not existing')
    quit()

show_from_msgs = {}

for line in file_handle :

    if line.startswith('From') :

        split_str_by_space = line.split(' ')
        split_email_by_at_symbol = split_str_by_space[1].split('@')
        
        try :
            date_ind = split_str_by_space[2]
            show_from_msgs[split_email_by_at_symbol[0]] = f'It was received on {split_str_by_space[2]}'
        except IndexError :
            continue


for item in show_from_msgs.items() :
    out = f'The user {item[0]} send an email on {item[1]}!'
    print(out)
        
