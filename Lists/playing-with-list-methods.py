names = [
    ('Ventsislav', 'Iliev'),
    ('Gosho', 'Petkov')
]

all_employees = []

for name in names:
    to_list = list(name)
    all_employees.append(to_list)

    find_name = all_employees.index(to_list)
    all_employees.append(' '.join(all_employees[find_name]))
    all_employees.pop(find_name)

print(all_employees)
