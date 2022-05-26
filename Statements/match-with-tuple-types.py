tuple_type = ('petko', 'georgiev')
# tuple_type = ('ventsi', 'iliev')
greeting = ''

def uppercase_first(v) :
    out = v[0].upper() + v[1:]
    return out

match tuple_type :
    case (x, 'iliev') :
        if x == 'ventsi' :
            greeting = 'Hello {name} Iliev!'.format(name = uppercase_first(x))
    case (x, y) :
        greeting = 'Hello {first} {last}! You\'ve come to a first time in here!'.format(first = uppercase_first(x), last = uppercase_first(y))
    case _ :
        print('The name is not recognized')

print(greeting)
