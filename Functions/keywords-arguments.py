def person_salary(salary, **kwargs):
    out = ''

    for k in kwargs:
        if k == 'position':
            break
        out += kwargs[k]

    print('{out} was getting this salary: {salary}! Position: {pos}!'.format(out=out, salary=salary, pos=kwargs['position']))


name = input('Your name: \n')
pos = input('Position: \n')
person_salary(3000, name=name, position=pos)