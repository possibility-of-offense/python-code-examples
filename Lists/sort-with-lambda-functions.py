people = [
    {"name": 'Petko', "salary": 104200},
    {"name": 'Gosho', "salary": 1000}
]

people.sort(key = lambda person : person.get('salary'))

print(people)