word = 'This is some word sent by this email blah@      blah.bg on some date in the future'

def find_word(w) :
    start_pos = w.find('@')
    email = ''

    if start_pos == -1 :
        print('Not found')
        exit()

    found_char = False

    for ind in range(len(w[start_pos:])) :
        char = w[start_pos + 1:][ind]

        if char == ' ' and found_char == False:
            found_char = False
            continue
        else :
            found_char = True
        
        if found_char == True :
            if char == ' ':
                break
            else :
                email += char
    
    print(f'The email is {email}!')

find_word(word)