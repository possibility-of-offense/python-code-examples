largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    num_int = 0

    try :
        if num != 'done' :
            num_int = int(num)
    except :
        print('Invalid character')
        continue

    if num == "done":
        break
    elif smallest is None and largest is None :
        smallest = int(num_int)
        largest = int(num_int)
    else :
        if int(num_int) > largest :
            largest = num_int
        elif int(num_int) < smallest :
            smallest = num_int

print("Maximum", largest)
print("Minimum", smallest)