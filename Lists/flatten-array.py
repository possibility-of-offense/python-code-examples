def flatten_array(arr) :
    new_arr = []

    for item in arr :
        if isinstance(item, list) :
            for new_item in item :
                if isinstance(new_item, list) :
                   new_arr.extend(flatten_array(new_item))
                else :
                   new_arr.append(new_item)
        else :
            new_arr.append(item)

    return new_arr



returned_arr = flatten_array([[1, [6, [3, 4, [5]], [3, 4]]]])
print(returned_arr)