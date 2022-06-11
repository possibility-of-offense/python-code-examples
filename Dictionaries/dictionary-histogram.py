names = ['gosho', 'petko', 'gosho', 'ventsi', 'nikolai', 'ventsi', 'karamfil', 'ventsi', 'nikolai', 'ventsi']
count_names = dict()

for name in names :
    if name in count_names :
        count_names[name] = count_names[name] + 1
    else :
        count_names[name] = 1

print(count_names)