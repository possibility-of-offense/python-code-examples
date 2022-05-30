def detect_done() :
    count = 0
    total = 0

    while True :
        inp = input('Enter a number: ')

        if inp == 'done' :
            break

        try :
            inp_parset_to_int = int(inp)

            count = count + 1
            total = total + inp_parset_to_int
        except :
            print('Invalid character')
            continue

    print(f'Total {total}')
    print(f'Count {count}')
    print('Avg {cond}'.format(cond = total / count if total > 0 else 'No total and count yet!'))

detect_done()