people = ['Nikolai', 'Gosho', 'Ventsislav', 'Petko']

def search_by_name(group, name) :
    if name in group :
        return name

def set_team_leader(group) :
    found = search_by_name(group, 'Ventsislav')

    return [person.upper() if person == found else person for person in group]

new_people = set_team_leader(people)
print(new_people)

