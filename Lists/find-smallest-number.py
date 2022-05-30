def find_smallest(numbers):
    ind = 0
    smallest = 0

    for i in numbers :
        if ind == 0 :
            smallest = i
        
        if i < smallest :
            smallest = i

        ind = ind + 1
    
    return smallest

numbers = [9, 41, 12, 3, 74, 15]

smallest = find_smallest(numbers)
print(smallest)