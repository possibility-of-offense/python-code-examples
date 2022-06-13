file_handle = open('mail-example.txt')
addresses = dict()
hours = dict()

for line in file_handle :
    if not line.startswith('From') :
        continue
    else :
        strip_line = line.rstrip()
        split_line = strip_line.split(' ')
        email_addr = split_line[1].split('@')[0]

        try :
            hour = split_line[5].split(':')[0]
            hours[hour] = hours.get(hour, 0) + 1
        except :
            pass

        

        if email_addr in addresses :
            addresses[email_addr] += 1
        else :
            addresses[email_addr] = 1

list_addresses = sorted([(v, k) for (k, v) in addresses.items()], reverse = True)

for (cnt, address) in list_addresses :
    print(f'{address} has been mentioned {cnt} times!')

for (t, h) in hours.items() :
    print(f'The hour of {t} has a frequency of {h}!')