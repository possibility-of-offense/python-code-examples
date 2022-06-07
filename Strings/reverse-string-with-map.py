def reverse_str (name) :
    rev_name = ''.join(map(lambda x: x.upper(), reversed(name)))
    print(rev_name)

your_name = input('Enter your name: \n')

reverse_str(name = your_name)