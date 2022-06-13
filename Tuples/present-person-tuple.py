(name, info) = ('ventsislav iliev', {"DOB": "28-02-1990"})

def get_name(n) :
    split_name = n.split(' ')
    first_name = split_name[0]
    prefix = 'Mr.' if first_name[len(first_name) - 1] != 'a' else 'Ms.'

    return '{prefix}{name}'.format(prefix = prefix, name = first_name.capitalize()) 

def get_age(age) :
    return age.replace('-', '/')

is_me = True

def present_person(name_of_person = 'John Doe', dob = 'unknown') :
    if type(is_me) == bool : 
        name_of_person = 'ventsislav iliev'

    out = '{name} was born on {age}!'.format(name = get_name(name_of_person), age = get_age(dob))
    return (name_of_person, out)

person = present_person(dob = info['DOB'])

print(f'The full name is {person[0]} and the message is "{person[1]}"')