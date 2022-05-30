def detect_done() :
    count = 0
    total = 0
    min = None
    max = None

    while True :
        inp = input('Enter a number: ')

        if inp == 'done' :
            break

        try :
            inp_parset_to_int = int(inp)

            if min is None and max is None :
                min = inp_parset_to_int
                max = inp_parset_to_int
            else :
                if inp_parset_to_int < min :
                    min = inp_parset_to_int
                elif inp_parset_to_int > max :
                    max = inp_parset_to_int

            count = count + 1
            total = total + inp_parset_to_int
        except :
            print('Invalid character')
            continue

    print(f'Total {total}')
    print(f'Count {count}')
    print('Avg {cond}'.format(cond = total / count if total > 0 else 'No total and count yet!'))
    print(f'Max {max}')
    print(f'Min {min}')

detect_done()