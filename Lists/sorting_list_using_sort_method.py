def sort_list(l, cb) :
    l.sort(key = cb)

def sort_list_cb(p):
    return p

new_l = ['b', 'a', 1]
new_l_copy = new_l.copy()

for i in range(len(new_l_copy)) :
    if type(new_l_copy[i]) != str :
        new_l.remove(new_l_copy[i])
    

sort_list(new_l,sort_list_cb)

print(new_l)