fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    new_line = line.rstrip().split()

    for l in new_line :
        if l in lst :
            continue
        else :
            lst.append(l)

sorted_list = sorted(lst, key=str.casefold)
print(sorted_list)