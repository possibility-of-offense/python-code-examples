names = ['gosho', 'petko', 'gosho', 'ventsi', 'nikolai', 'ventsi', 'karamfil', 'ventsi', 'nikolai', 'ventsi']
count_names = dict()

for name in names :
    count_names[name] = count_names.get(name, 0) + 1

    # if name in count_names :
    #     count_names[name] = count_names[name] + 1
    # else :
    #     count_names[name] = x

new_dict = dict()
for key in count_names.keys() :
    if key.startswith('g') :
        continue
    else :
        new_dict[key] = count_names[key]

print(new_dict)