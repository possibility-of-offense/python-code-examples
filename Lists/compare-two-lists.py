list1 = [1, 2, 3, 4]
list2 = [1, 3, 4, 5]

def compare_lists(a, b) :

    output = False
    firsts_not_equal_elements = ()

    for ind, val in enumerate(a) :
        if val == b[ind] :
            output = True
        else :
            output = False
            firsts_not_equal_elements = (val, b[ind])

            break

    first, second = firsts_not_equal_elements

    returned_out =  f'{a} is not equal to {b}' if output == False else f'{a} is equal to {b}! '
    returned_out += f' The different elements are {" and ".join(map(lambda x: str(x), list(firsts_not_equal_elements)))}!'

    return returned_out
            
file_handle = open('../lists.txt')

lists = []

for line in file_handle :
    
    build_list = ''
    ind = line.index('=')
    sliced_str = line[ind + 1:]
    lists.append(sliced_str.strip())

    for char in line :
        if char != '[' :
            continue
        else :
            build_list += char


c = compare_lists(*lists)
print(c)