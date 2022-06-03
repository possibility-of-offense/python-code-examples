# ../employees.csv
import re

def read_from_a_file(f) :
    find_common_projects = {}

    try :
        file_handle = open(f)
    except :
        print('The file is not existing')
        quit()

    for line in file_handle :
        line = line.rstrip()
        
        split_line_by_space = line.split(' ')

        for i in split_line_by_space :
            try :                
                get_project_name = i.split(' ')

                for word in get_project_name :
                    result = re.match("[-+]?\d+$", word)

                    if result is not None :
                        to_int = int(word)
                        get_next_values = split_line_by_space.index(word)
                        sliced_list = split_line_by_space[get_next_values + 1:]
                        
                        build_key = '-'.join(sliced_list).lower()
                        if build_key in find_common_projects :
                            find_common_projects[build_key].append(split_line_by_space[0])
                        else :
                            find_common_projects[build_key] = [split_line_by_space[0]]
                            

                    else :
                        continue

            except :
                continue

    unique_projects = []
    for item in find_common_projects.items() :
        if len(item[1]) > 1 :
            unique_projects.append(item)

    return unique_projects

inp = input("Enter a file name: \n")

unique = read_from_a_file(inp)

ind = 0
while ind < len(unique) :
    members = ' and '.join(unique[ind][1]) 
    formatted_str = unique[ind][0].replace('\'', ' | ')
    formatted_str = formatted_str.upper()

    print(f'The unique project is{formatted_str}and the members are {members}!')
    ind = ind + 1