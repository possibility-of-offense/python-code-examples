def clone_split(sequence, delimiter) :

    temp_list = []
    list_to_return = []

    for i in sequence: 
        if delimiter == i :
            
            continue
        else :
            temp_list.append(i)

    for val in temp_list :
        try :
            to_int = int(val)
            list_to_return.append(to_int)
        except :
            continue

    return list_to_return


cloned = clone_split('1,,,,,,5,1,3,5,da,dobre sum,', ',')
print(cloned)