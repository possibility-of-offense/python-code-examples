person = 'Ventsislav', 'Iliev', 32, {"job": "jobless"}
earned_money = [100, '300', 500, 205]

def unpack_tuple_4_elements(t, e) :
    name, last_name, age, job = t
    job_value = len(job) > 0 and job['job']

    earn = ''.join(list(str(sum([int(el) for el in e]))))

    greeting = f'My name is {name} {last_name}! My age is {age} and my job is {job_value}! {earn}!'
    print(greeting)

unpack_tuple_4_elements(person, earned_money)