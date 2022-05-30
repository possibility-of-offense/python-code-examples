numbers = [3, 41, 12, 9, 74, 15]
largest = 0

for numb in numbers :
    ind = numbers.index(numb)
    if ind == 0 :
        largest = numb
    else :
        if numb > largest :
            largest = numb

print(largest)