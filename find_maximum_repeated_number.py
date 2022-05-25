repeated_numbers = {
    '1': 4,
    '2': 3,
    '11': 1,
    '7': 2,
    '9': 11
}

find_max_repeated_numbers = []

for numb in repeated_numbers:
    if len(find_max_repeated_numbers) == 0:
        formatted_str = '{key} {value}'.format(key = numb, value = repeated_numbers[numb])
        find_max_repeated_numbers.append(formatted_str)
    else:
        get_key = find_max_repeated_numbers[0].split()[0]
        get_value = find_max_repeated_numbers[0].split()[1]
        
        if repeated_numbers[numb] > int(get_value):
            formatted_str = '{key} {value}'.format(key = numb, value = repeated_numbers[numb])
            find_max_repeated_numbers[0] = formatted_str

print('The number which has been repeated maximum times is {n}!'.format(n = find_max_repeated_numbers[0].split()[0]))

