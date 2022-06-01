a = [1, 2, 3]
b = []

for ind in range(len(a) + 1) :
    if ind < len(a) :
        b.append(a[ind])
    else :
        
        for k in range(len(a)) :
            b.append(a[len(a) - 1 - k])
        break

print(b)