# Get imaginary median calculated by the characters of the some words!

def get_median(l) :
    len_l = len(l)
    get_middle = int(len_l / 2)

    if len_l % 2 != 0 :
        
        print('The median of this list is {median}!'.format(median = l[get_middle - 1]))
        return
    else :
        list1 = l[0:get_middle]
        list2 = l[get_middle:]

        if len(list1) != len(list2) :
            print('Something is wrong! The lengths of the lists are not equal')
        
        els = []
        els.append(list1[len(list1) - 1])
        els.append(list2[0])
        
        els = list(map(lambda x: len(x), els))
        
        max_count = 0
        els_len = len(els)

        for val in range(els_len) :
            max_count = max_count + els[val]

        print('The median of this fictional words (being calculated by the length of them) is {med}!'.format(med = max_count / els_len))
        


get_median(["green",
"green",
"green1",
"green1",
])

# get_median(["green",
# "green",
# "green",
# "green",
# "yellow",
# "green",
# "yellow",
# "yellow 5",
# "yellow",
# "yellow",
# "yellow",
# "yellow",
# "red",
# "green",
# "red",  
# "yellow"])