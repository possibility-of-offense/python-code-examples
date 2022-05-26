def get_name(name: str) -> str:
    out = ''

    if type(name) != str:
        print('Not a string')
    else :
        out = 'Your name is ' + name
    if 'return' in get_name.__annotations__:
        if (get_name.__annotations__['return']) == str and type(out) != str :
            print('Wrong output type')
        else :
            print(out)


get_name('Ventsi')