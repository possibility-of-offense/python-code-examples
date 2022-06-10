# First solution

number_of_times = int(input())

while number_of_times > 0 :

    str_to_check = input()
    chars_to_check = [',', '.', '_']
    pure = True

    for ind, val in enumerate(str_to_check) :
        if chars_to_check.count(val) > 0 :
            pure = False
            break

    out = f'{str_to_check} is pure.' if pure else f'{str_to_check} is not pure!'
    print(out)

    number_of_times = number_of_times - 1

# Second solution

number_of_times = int(input())

while number_of_times > 0 :

    str_to_check = input()
    pure = True

    if ',' in str_to_check or '.' in str_to_check or '_' in str_to_check :
        pure = False


    out = f'{str_to_check} is pure.' if pure else f'{str_to_check} is not pure!'
    print(out)

    number_of_times = number_of_times - 1

